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


def generate_resume(author: Author, output_dir: str):
    # generate resume and output to file and standard output
    resume: Resume = Resume(author)
    resume.build(f"Resume_{resume.author.name.replace(' ', '_')}.md", output_dir)
    print(resume)
