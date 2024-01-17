import subprocess

from src.resume.components.author import Author
from src.resume.components.resume import Resume


def xp_fmt(name, address, spec, date):
    return (
        "<div class='xp-h'>"
        + f"<span>{name}</span>"
        + f"<span>{address}</span>"
        + "</div>\n"
        + "<div class='xp-s'>"
        + f"<span>{spec}</span>"
        + f"<span>{date}</span>"
        + "</div>"
    )


def md_to_pdf(
    md_file: str,
    pdf_file: str,
    html_template: str = "./src/template/resume.html",
    css_template: str = "./src/template/resume.css",
):
    subprocess.run(
        [
            "pandoc",
            md_file,
            "-t",
            "html",
            f"--template={html_template}",
            f"--css={css_template}",
            "--metadata=title:Resume",
            "--variable",
            "papersize=letter",
            "--variable",
            "margin-top=0",
            "--variable",
            "margin-right=0",
            "--variable",
            "margin-bottom=0",
            "--variable",
            "margin-left=0",
            "--pdf-engine-opt=--enable-local-file-access",
            "-o",
            pdf_file,
        ]
    )


def generate_resume(author: Author, output_dir: str):
    # generate resume and output to file and standard output
    resume: Resume = Resume(author)
    filename = f"Resume_{resume.author.name.replace(' ', '_')}"
    resume.build(f"{filename}.md", output_dir)
    md_to_pdf(
        f"{output_dir.rstrip('/')}/{filename}.md",
        f"{output_dir.rstrip('/')}/{filename}.pdf",
    )
    print(resume)
