from dataclasses import dataclass
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
    with open(resume_yaml.filename, "wb") as buffer:
        copyfileobj(resume_yaml.file, buffer)

    # Convert YAML to PDF
    proc = run(
        f"bash resumake.sh {resume_yaml.filename} {margin}",
        shell=True,
        check=True,
        capture_output=True,
        encoding="utf-8",
    )

    # Return generated file metadata
    filepath = proc.stdout.strip()
    filename = filepath.split("/")[-1]
    return Resume(filename, filepath)
