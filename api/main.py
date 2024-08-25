from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse

from .utils import generate_resume_pdf

app = FastAPI()


@app.post("/resume/")
async def process_resume(resume_yaml: UploadFile) -> FileResponse:
    resume_metadata = generate_resume_pdf(resume_yaml)

    # To view the file in the browser, use "inline" for the media_type
    headers = {
        "Content-Disposition": f"inline; filename={resume_metadata.filename}",
    }

    # Return FileResponse object with the file path, media type and headers
    return FileResponse(
        resume_metadata.filepath, media_type="application/pdf", headers=headers
    )
