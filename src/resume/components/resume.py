from src.resume.components.author import Author


class Resume:
    def __init__(self, author: Author):
        self.author = author

    def build(self, filename: str, output_dir: str):
        with open(output_dir + filename, "w") as file:
            file.write(str(self))

    def __str__(self) -> str:
        return "\n\n".join(
            [
                self.header,
                self.skills,
                self.experience,
                self.projects,
                self.education,
            ]
        )

    @property
    def header(self) -> str:
        return repr(self.author)

    @property
    def skills(self) -> str:
        return "## Skills & Interests\n\n" + "  \n".join(
            [str(skill) for skill in self.author.skills]
        )

    @property
    def projects(self) -> str:
        return "## Project Experience\n\n" + "\n\n".join(
            [str(project) for project in self.author.projects]
        )

    @property
    def experience(self) -> str:
        return "## Work Experience\n\n" + "\n\n".join(
            [str(experience) for experience in self.author.experiences]
        )

    @property
    def education(self) -> str:
        return f"## Education\n\n{self.author.education}"
