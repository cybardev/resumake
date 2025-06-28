package main

import (
	_ "embed"
	"flag"
	"fmt"
	"html/template"
	"io"
	"log"
	"mime/multipart"
	"net/http"
	"os"
	"os/exec"
	"strings"

	"gopkg.in/yaml.v3"
)

// Embedded files
//
//go:embed resources/template.go.tmpl
var goTemplate string

//go:embed resources/error.go.tmpl
var errorTemplate string

//go:embed resources/template.css
var cssTemplate string

//go:embed resources/index.html
var indexPage string

// Constants
const PDF_FILE = "Resume.pdf"
const HTML_TEMPLATE = "template.html"
const CSS_TEMPLATE = "template.css"

func main() {
	// CLI arg for server port
	var port int
	flag.IntVar(&port, "p", 80, "Port number to serve on")
	flag.Parse()

	// HTTP handlers
	http.HandleFunc("/", serveIndexPage)
	http.HandleFunc("/resume/", resumakeHandler)

	// Start server
	log.Printf("Starting server on port %d...", port)
	err := http.ListenAndServe(fmt.Sprintf(":%d", port), nil)
	if err != nil {
		log.Fatalf("Error starting server: %v", err)
	}
}

func serveIndexPage(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "text/html")
	w.WriteHeader(http.StatusOK)
	w.Write([]byte(indexPage))
}

func resumakeHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}

	file, _, err := r.FormFile("resume")
	if err != nil {
		handleError(w, &YAMLValidationError{"Invalid YAML file provided"})
		return
	}
	defer file.Close()

	tmpl, err := template.New("resume").Funcs(template.FuncMap{
		"join": strings.Join,
	}).Parse(goTemplate)
	if err != nil {
		handleError(w, err)
		return
	}

	err = htmlgen(file, tmpl)
	if err != nil {
		handleError(w, err)
		return
	}

	err = os.WriteFile(CSS_TEMPLATE, []byte(cssTemplate), 0644)
	if err != nil {
		handleError(w, err)
		return
	}

	outfile := PDF_FILE
	cmd := pdfgen(outfile)
	err = cmd.Run()
	if err != nil {
		handleError(w, err)
		return
	}

	w.Header().Set("Content-Disposition", fmt.Sprintf("inline; filename=%s", outfile))
	w.Header().Set("Content-Type", "application/pdf")
	http.ServeFile(w, r, outfile)
}

func pdfgen(outputFile string) exec.Cmd {
	cmd := exec.Command(
		"weasyprint",
		HTML_TEMPLATE, // Path to the generated HTML file
		outputFile,    // Path to the output PDF file
		"-s",          // Specify the CSS file
		CSS_TEMPLATE,  // Path to the CSS file
	)
	cmd.Stdin = os.Stdin
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr

	return *cmd
}

func htmlgen(f multipart.File, t *template.Template) error {
	// destination
	dst, err := os.Create(HTML_TEMPLATE)
	if err != nil {
		return err
	}
	defer func() {
		if cerr := dst.Close(); cerr != nil && err == nil {
			err = cerr
		}
	}()

	// populate resume struct
	bytes, err := io.ReadAll(f)
	if err != nil {
		return err
	}
	r := Resume{}
	err = yaml.Unmarshal(bytes, &r)
	if err != nil {
		return err
	}
	err = r.Validate()
	if err != nil {
		return &YAMLValidationError{err.Error()}
	}

	// populate template
	err = t.Execute(dst, r)
	if err != nil {
		return err
	}

	return nil
}

func handleError(w http.ResponseWriter, err error) {
	code := http.StatusInternalServerError
	msg := "Server Error: There has been an error on the server side."

	switch e := err.(type) {
	case *YAMLValidationError:
		code = http.StatusUnprocessableEntity
		msg = fmt.Sprintf("YAML Validation Error: %s", e.Msg)
	default:
		if code >= 400 && code < 500 {
			msg = "Client Error: There has been an error on the client side."
		}
	}

	// Create a new error page
	ep, tmpErr := NewErrorPage(code, http.StatusText(code), msg, code >= 400 && code < 500)
	if tmpErr != nil {
		log.Printf("Error generating error page: %v", tmpErr)
		http.Error(w, "Internal Server Error", http.StatusInternalServerError)
		return
	}

	// Generate the error page content in memory
	var errorPageContent strings.Builder
	tmpErr = ep.Tmpl.Execute(&errorPageContent, ep)
	if tmpErr != nil {
		log.Printf("Error generating error page: %v", tmpErr)
		http.Error(w, "Internal Server Error", http.StatusInternalServerError)
		return
	}

	// Serve the generated error page
	w.Header().Set("Content-Type", "text/html")
	w.WriteHeader(code)
	w.Write([]byte(errorPageContent.String()))
}

type YAMLValidationError struct {
	Msg string
}

func (e *YAMLValidationError) Error() string {
	return e.Msg
}

type ErrorPage struct {
	Code      int
	Header    string
	Msg       string
	UserError bool
	Tmpl      *template.Template
}

func NewErrorPage(code int, header string, msg string, uerr bool) (*ErrorPage, error) {
	tmpl, err := template.New("error").Parse(errorTemplate)
	if err != nil {
		return &ErrorPage{}, err
	}
	ep := ErrorPage{code, header, msg, uerr, tmpl}
	return &ep, nil
}

func (p *ErrorPage) Update(code int, header string, msg string, uerr bool) {
	p.Code = code
	p.Header = header
	p.Msg = msg
	p.UserError = uerr
}

func (p ErrorPage) Generate() error {
	// destination
	dst, err := os.Create("error.html")
	if err != nil {
		return err
	}
	defer func() {
		if cerr := dst.Close(); cerr != nil && err == nil {
			err = cerr
		}
	}()

	// populate template
	err = p.Tmpl.Execute(dst, p)
	if err != nil {
		return err
	}

	return nil
}
