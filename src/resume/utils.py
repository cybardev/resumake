import os
import subprocess

from .components.resume import Resume


def xp_fmt(name: str, address: str, spec: str, date: str) -> str:
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
    filename: str,
    html_template: str = "./template/resume.html",
    css_template: str = "./template/resume.css",
) -> None:
    html_template = os.path.abspath(html_template)
    css_template = os.path.abspath(css_template)
    subprocess.run(
        [
            "pandoc",
            f"{filename}.md",
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
            f"{filename}.pdf",
        ]
    )


def pdf_to_png(
    filename: str,
) -> None:
    subprocess.run(
        ["pdftoppm", "-png", "-singlefile", f"{filename}.pdf", filename]
    )


def generate_resume(resume, output_dir: str):
    # generate resume and output to markdown file
    filename = (
        output_dir.rstrip("/")
        + "/"
        + f"Resume_{resume.author.name.replace(' ', '_')}"
    )
    resume.build(f"{filename}.md")

    # convert markdown to pdf and generate png image
    md_to_pdf(filename)
    pdf_to_png(filename)

    return resume
