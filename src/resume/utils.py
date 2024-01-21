import os
import subprocess


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


def md_to_pdf(filename: str, html_template: str, css_template: str) -> None:
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
            f"--metadata=title:{filename}",
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


def pdf_to_png(filename: str) -> None:
    # check number of pages in pdf
    pdfinfo = subprocess.check_output(("pdfinfo", f"{filename}.pdf"))
    pages = int(pdfinfo.decode("utf-8").split("Pages: ")[1].split("\n")[0])

    conversion_cmd = ["pdftoppm", "-png", f"{filename}.pdf", filename]

    if pages == 1:
        # output a single image without page number in name
        conversion_cmd.insert(2, "-singlefile")

    subprocess.run(conversion_cmd)


def generate_resume(
    resume, output_dir: str, html_template: str, css_template: str
):
    # generate markdown from python resume script
    filename = (
        output_dir.rstrip("/")
        + "/"
        + f"Resume_{resume.author.name.replace(' ', '_')}"
    )
    resume.build(f"{filename}.md")

    # convert markdown to pdf and generate png image
    md_to_pdf(filename, html_template, css_template)
    pdf_to_png(filename)

    return resume
