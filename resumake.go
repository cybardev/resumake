package main

import (
	"flag"
	"fmt"
	"html/template"
	"io"
	"mime/multipart"
	"net/http"
	"os"
	"os/exec"
	"path"
	"strings"

	"gopkg.in/yaml.v3"
)

// file names
const (
	GO_TEMPLATE    string = "resources/template.go.tmpl"
	ERROR_TEMPLATE string = "resources/error.go.tmpl"
	HTML_TEMPLATE  string = "resources/template.html"
	CSS_TEMPLATE   string = "resources/template.css"
	INDEX_PAGE     string = "static/site/index.html"
	ERROR_PAGE     string = "static/site/error.html"
	PDF_FILE       string = "Resume.pdf"
)

func main() {
	// CLI arg for server port
	var port int
	flag.IntVar(&port, "p", 80, "Port number to serve on")
	flag.Parse()

	// HTTP handlers
	http.HandleFunc("/", serveIndexPage)
	http.HandleFunc("/resume/", resumakeHandler)

	// Start server
	fmt.Printf("Starting server on port %d...\n", port)
	err := http.ListenAndServe(fmt.Sprintf(":%d", port), nil)
	if err != nil {
		fmt.Printf("Error starting server: %v\n", err)
	}
}

func serveIndexPage(w http.ResponseWriter, r *http.Request) {
	http.ServeFile(w, r, INDEX_PAGE)
}

func resumakeHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}

	file, _, err := r.FormFile("resume")
	if err != nil {
		handleError(w, r, &YAMLValidationError{"Invalid YAML file provided"})
		return
	}
	defer file.Close()

	tmpl, err := template.New(path.Base(GO_TEMPLATE)).Funcs(template.FuncMap{
		"join": strings.Join,
	}).ParseFiles(GO_TEMPLATE)
	if err != nil {
		handleError(w, r, err)
		return
	}

	err = htmlgen(file, tmpl)
	if err != nil {
		handleError(w, r, err)
		return
	}

	outfile := PDF_FILE
	cmd := pdfgen(outfile)
	err = cmd.Run()
	if err != nil {
		handleError(w, r, err)
		return
	}

	w.Header().Set("Content-Disposition", fmt.Sprintf("inline; filename=%s", outfile))
	w.Header().Set("Content-Type", "application/pdf")
	http.ServeFile(w, r, outfile)
}

func pdfgen(f string) exec.Cmd {
	cmd := exec.Command(
		"weasyprint",
		"-s",
		CSS_TEMPLATE,
		HTML_TEMPLATE,
		f,
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

func handleError(w http.ResponseWriter, r *http.Request, err error) {
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

	ep, tmpErr := NewErrorPage(code, http.StatusText(code), msg, code >= 400 && code < 500)
	if tmpErr != nil {
		fmt.Printf("Error generating error page: %v\n", tmpErr)
		http.Error(w, "Internal Server Error", http.StatusInternalServerError)
		return
	}

	tmpErr = ep.Generate()
	if tmpErr != nil {
		fmt.Printf("Error generating error page: %v\n", tmpErr)
		http.Error(w, "Internal Server Error", http.StatusInternalServerError)
		return
	}

	http.ServeFile(w, r, ERROR_PAGE)
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
	tmpl, err := template.ParseFiles(ERROR_TEMPLATE)
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
	dst, err := os.Create(ERROR_PAGE)
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
