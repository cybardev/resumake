from fastapi import FastAPI, UploadFile, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

from .utils import generate_resume_pdf

app = FastAPI()
templates = Jinja2Templates(directory="./static/site")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/resume/")
async def process_resume(resume: UploadFile) -> FileResponse:
    resume_file = generate_resume_pdf(resume)

    # To view the file in the browser, use "inline" for the media_type
    headers = {
        "Content-Disposition": f"inline; filename={resume_file}",
    }

    # Return FileResponse object with the file path, media type and headers
    return FileResponse(resume_file, media_type="application/pdf", headers=headers)
