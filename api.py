import errno
import os

from pathlib import Path
from shutil import copyfileobj
from subprocess import run
from typing import Annotated

from fastapi import FastAPI, File, Form, UploadFile, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

# --- SERVER --- #

app = FastAPI()
templates = Jinja2Templates(directory="static/site")


@app.get("/", response_class=HTMLResponse)
async def client(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/resume/")
async def process_resume(
    resume: Annotated[UploadFile, File()], margin: Annotated[int, Form()]
):
    resume_pdf: str = generate_resume_pdf(resume, margin)

    # To view the file in the browser, use "inline" for the media_type
    headers = {
        "Content-Disposition": f"inline; filename={resume_pdf}",
    }

    # Return FileResponse object with the file path, media type and headers
    return FileResponse(resume_pdf, media_type="application/pdf", headers=headers)


@app.exception_handler(FileNotFoundError)
async def internal_server_error_handler(request: Request, exc: FileNotFoundError):
    return templates.TemplateResponse(
        request=request, name="error.html", context={"err_code": 500}, status_code=500
    )


@app.exception_handler(KeyError)
async def unprocessable_content_handler(request: Request, exc: KeyError):
    return templates.TemplateResponse(
        request=request, name="error.html", context={"err_code": 422}, status_code=422
    )


# --- UTILS --- #


def generate_resume_pdf(resume_yaml: UploadFile, margin: int) -> str:
    # Save resume.yml to server
    with open(resume_yaml.filename, "wb") as buffer:
        copyfileobj(resume_yaml.file, buffer)

    with open(resume_yaml.filename) as yaml_file, open("_resume.md", "w") as config:
        # cache author name
        yaml = yaml_file.readlines()
        try:
            author_line = next(s for s in yaml if s.startswith("author: "))
        except StopIteration:
            raise KeyError("author")
        author = author_line.split(": ")[-1].replace(" ", "_").rstrip()

        # create Markdown source from YAML
        config.write("---\n")
        config.writelines(yaml)
        config.write("---\n")

    # Convert YAML to PDF
    pdf_filename = f"Resume_{author}.pdf"
    run(
        [
            "pandoc",
            "-s",
            "_resume.md",
            "-t",
            "html",
            "--template=resources/template.html",
            f"--metadata=title:Resume_{author}",
            "--variable",
            "papersize=letter",
            "--variable",
            f"margin-top={margin}",
            "--variable",
            "margin-right=0",
            "--variable",
            "margin-bottom=0",
            "--variable",
            "margin-left=0",
            "--pdf-engine=wkhtmltopdf",
            "--pdf-engine-opt=--enable-local-file-access",
            "-o",
            pdf_filename,
        ]
    )

    if Path(pdf_filename).is_file(follow_symlinks=False):
        return pdf_filename
    else:
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), pdf_filename)
