import os
from pathlib import Path


class Resume:
    def __init__(self, author, schema: str):
        self.author = author

        # set up schema
        full_schema = {
            "profile": self.profile,
            "skills": self.skills,
            "experience": self.experience,
            "projects": self.projects,
            "education": self.education,
        }
        self._schema = [
            full_schema[section.strip()] for section in schema.split(",")
        ]

    def build(self, filename: str):
        """Generate resume in markdown format and save to file

        Args:
            filename (str): name of file to save resume to (including path)
        """
        # ensure path exists and file can be created
        path = Path(os.path.abspath(filename))
        path.parent.mkdir(parents=True, exist_ok=True)

        with open(filename, "w") as file:
            file.write(str(self))

    def __str__(self) -> str:
        return "\n\n".join([self.header, *self._schema])

    @property
    def header(self) -> str:
        return repr(self.author)

    @property
    def profile(self) -> str:
        return (
            f"## Career Profile\n\n{self.author.profile}"
            if self.author.profile is not None
            else ""
        )

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
