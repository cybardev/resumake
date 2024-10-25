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

func main() {
	app := echo.New()
	app.File("/", "static/site/index.html")
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
	outfile := "Resume.pdf"
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
		"resources/template.css",
		"resources/template.html",
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
	dst, err := os.Create("resources/template.html")
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
	tmpl, err := template.ParseFiles("resources/template.go.tmpl")
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
	errorPage := fmt.Sprintf("static/site/%d.html", code)
	if err := c.File(errorPage); err != nil {
		c.Logger().Error(err)
	}
}
