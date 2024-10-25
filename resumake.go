package main

import (
	"fmt"
	"io"
	"mime/multipart"
	"net/http"
	"os"
	"os/exec"

	"github.com/labstack/echo/v4"
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
	err = saveFile(file)
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
		"pandoc",
		"-s",
		"_resume.md",
		"-t",
		"html",
		"--template=resources/template.html",
		"--metadata=title:Resume",
		"--pdf-engine=weasyprint",
		"-o",
		f,
	)
	cmd.Stdin = os.Stdin
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr

	return *cmd
}

func saveFile(f *multipart.FileHeader) error {
	// source
	src, err := f.Open()
	if err != nil {
		return err
	}
	defer src.Close()

	// destination
	dst, err := os.Create("_resume.md")
	if err != nil {
		return err
	}
	defer dst.Close()

	// copy
	_, err = dst.WriteString("---\n")
	if err != nil {
		return err
	}
	_, err = io.Copy(dst, src)
	if err != nil {
		return err
	}
	_, err = dst.WriteString("---\n")
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
