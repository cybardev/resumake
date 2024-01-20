import os
from pathlib import Path


class Resume:
    def __init__(self, author):
        self.author = author

    def build(self, filename: str):
        # ensure path exists and file can be created
        path = Path(os.path.abspath(filename))
        path.parent.mkdir(parents=True, exist_ok=True)

        with open(filename, "w") as file:
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
    def experience(self) -> str:
        return "## Work Experience\n\n" + "\n\n".join(
            [str(experience) for experience in self.author.experiences]
        )

    @property
    def projects(self) -> str:
        return "## Project Experience\n\n" + "\n\n".join(
            [str(project) for project in self.author.projects]
        )

    @property
    def education(self) -> str:
        return f"## Education\n\n{self.author.education}"
