from fastapi import FastAPI

app = FastAPI()


@app.post("/resume")
def process_resume(resume_yaml: bytes) -> dict[str, bytes]:
    resume_pdf: bytes = generate_resume_pdf(resume_yaml)
    return {"resume_pdf": resume_pdf}


def generate_resume_pdf(data: bytes) -> bytes:
    # TODO: Implement PDF generation logic here
    resume = data
    return resume
