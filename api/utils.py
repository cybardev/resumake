from subprocess import run

from fastapi import UploadFile


def generate_resume_pdf(resume_yaml: UploadFile, margin: int) -> str:
    # Save resume.yml to server
    with open(f"_{resume_yaml.filename}", "wb") as buffer:
        contents = resume_yaml.file
        buffer.write(contents.read())

    # Store metadata for response
    contents.seek(0)
    resume = "Resume_" + b"_".join(contents.readline().split()[1:]).decode() + ".pdf"

    # Convert YAML to PDF
    run(
        f"bash resumake.sh _{resume_yaml.filename} {margin}",
        shell=True,
        check=True,
    )

    # clean up artifacts
    run(["rm", f"_{resume_yaml.filename}"])

    return resume
