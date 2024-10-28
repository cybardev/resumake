package main

import (
	"html/template"
	"io"
	"mime/multipart"
	"net/http"
	"os"
	"os/exec"

	"github.com/labstack/echo/v4"
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
	app := echo.New()
	app.File("/", INDEX_PAGE)
	app.POST("/resume/", resumake)
	app.HTTPErrorHandler = customHTTPErrorHandler
	app.Logger.Fatal(app.Start(":80"))
}

func resumake(c echo.Context) error {
	file, err := c.FormFile("resume")
	if err != nil {
		return &YAMLValidationError{"Invalid YAML file provided"}
	}
	err = htmlgen(file)
	if err != nil {
		return err
	}
	outfile := PDF_FILE
	cmd := pdfgen(outfile)
	err = cmd.Run()
	if err != nil {
		return err
	}

	return c.Inline(outfile, outfile)
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

func htmlgen(f *multipart.FileHeader) error {
	// source
	src, err := f.Open()
	if err != nil {
		return err
	}
	defer src.Close()

	// destination
	dst, err := os.Create(HTML_TEMPLATE)
	if err != nil {
		return err
	}
	defer dst.Close()

	// populate resume struct
	bytes, err := io.ReadAll(src)
	if err != nil {
		return err
	}
	r := Resume{}
	err = yaml.Unmarshal(bytes, &r)
	if err != nil {
		return err
	}
	isValid, msg := r.Validate()
	if !isValid {
		return &YAMLValidationError{msg}
	}

	// populate template
	tmpl, err := template.ParseFiles(GO_TEMPLATE)
	if err != nil {
		return err
	}
	err = tmpl.Execute(dst, r)
	if err != nil {
		return err
	}

	return nil
}

func customHTTPErrorHandler(err error, c echo.Context) {
	code := http.StatusInternalServerError
	if he, ok := err.(*echo.HTTPError); ok {
		code = he.Code
	}
	c.Logger().Error(err)
	// server error by default
	ep := &ErrorPage{
		code,
		"Server Error",
		"There has been an error on the server side.",
		false,
	}
	// check for user error
	switch e := err.(type) {
	case *YAMLValidationError:
		ep = &ErrorPage{
			422,
			"YAML Validation Error",
			e.Msg,
			true,
		}
	default:
		if 400 <= code && code < 500 {
			ep = &ErrorPage{
				code,
				"Client Error",
				"There has been an error on the client side.",
				true,
			}
		}
	}
	// create and return error page
	tmpErr := ep.Generate()
	if tmpErr != nil {
		c.Logger().Error(tmpErr)
	}
	if err := c.File(ERROR_PAGE); err != nil {
		c.Logger().Error(err)
	}
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
}

func (p *ErrorPage) Generate() error {
	// destination
	dst, err := os.Create(ERROR_PAGE)
	if err != nil {
		return err
	}
	defer dst.Close()

	// populate template
	tmpl, err := template.ParseFiles(ERROR_TEMPLATE)
	if err != nil {
		return err
	}
	err = tmpl.Execute(dst, p)
	if err != nil {
		return err
	}

	return nil
}
