from dataclasses import dataclass
from subprocess import run

from fastapi import UploadFile


@dataclass
class Resume:
    filename: str
    filepath: str


def generate_resume_pdf(resume_yaml: UploadFile) -> Resume:
    # Save resume.yml to server
    with open(resume_yaml.filename, "wb") as buffer:
        contents = resume_yaml.file
        buffer.write(contents.read())

    # Store metadata for response
    contents.seek(0)
    fname = (b"_".join(contents.readline().split()[1:]) + b".pdf").decode()
    resume = Resume(filename=fname, filepath=f"../{fname}")

    # Convert YAML to PDF
    run(
        f"bash resumake.sh {resume_yaml.filename}",
        cwd="..",
        shell=True,
        check=True,
    )

    return resume
