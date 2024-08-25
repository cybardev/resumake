from dataclasses import dataclass
from shutil import copyfileobj
from subprocess import run
from typing import Annotated

from fastapi import FastAPI, File, Form, UploadFile, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="static/site")

# --- SERVER --- #


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/resume/")
async def process_resume(
    resume: Annotated[UploadFile, File()], margin: Annotated[int, Form()]
) -> FileResponse:
    resume_metadata = generate_resume_pdf(resume, margin)

    # To view the file in the browser, use "inline" for the media_type
    headers = {
        "Content-Disposition": f"inline; filename={resume_metadata.name}",
    }

    # Return FileResponse object with the file path, media type and headers
    return FileResponse(
        resume_metadata.path, media_type="application/pdf", headers=headers
    )


# --- UTILS --- #


@dataclass
class Resume:
    name: str
    path: str


def generate_resume_pdf(resume_yaml: UploadFile, margin: int) -> Resume:
    # Save resume.yml to server
    with open(f"_{resume_yaml.filename}", "wb") as buffer:
        copyfileobj(resume_yaml.file, buffer)

    # Convert YAML to PDF
    proc = run(
        f"bash resumake.sh _{resume_yaml.filename} {margin}",
        shell=True,
        check=True,
        capture_output=True,
        encoding="utf-8",
    )

    # Clean up artifacts
    run(["rm", f"_{resume_yaml.filename}"])

    # Return generated file metadata
    filepath = proc.stdout.strip()
    filename = filepath.split("/")[-1]
    return Resume(filename, filepath)
