package main

import (
	"fmt"
	"html/template"
	"io"
	"log"
	"mime/multipart"
	"net/http"
	"os"
	"os/exec"

	"github.com/labstack/echo/v4"
	"gopkg.in/yaml.v3"
)

// file names
const (
	GO_TEMPLATE   string = "resources/template.go.tmpl"
	HTML_TEMPLATE string = "resources/template.html"
	CSS_TEMPLATE  string = "resources/template.css"
	INDEX_PAGE    string = "static/site/index.html"
	ERROR_PAGE    string = "static/site/%d.html" // %d is replaced by HTTP error code
	PDF_FILE      string = "Resume.pdf"
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
		return err
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
		// TODO: validate received YAML
		log.Println(err.Error())
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
	errorPage := fmt.Sprintf(ERROR_PAGE, code)
	if err := c.File(errorPage); err != nil {
		c.Logger().Error(err)
	}
}
