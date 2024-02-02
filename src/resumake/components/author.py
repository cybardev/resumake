from dataclasses import dataclass

from .address import Address
from .education import Education
from .experience import Experience
from .project import Project
from .skill import Skill


@dataclass(kw_only=True)
class Author:
    name: str
    address: Address
    phone: str
    email: str
    website: str
    social: str
    education: Education
    skills: list[Skill]
    projects: list[Project]
    experiences: list[Experience]
    profile: str = None

    def __repr__(self):
        return (
            f"# {self.name}\n\n"
            + "<header>\n"
            + f"<p>{str(self.address)}</p>\n"
            + "<section>\n"
            + f"<a href='tel:{self.__phone_fmt(self.phone)}'>{self.phone}</a>\n"
            + f"<a href='mailto:{self.email}'>{self.email}</a>\n"
            + f"<a href='https://{self.website}'>{self.website}</a>\n"
            + f"<a href='https://github.com/{self.social}'>github.com/{self.social}</a>\n"
            + f"<a href='https://www.linkedin.com/in/{self.social}'>linkedin.com/in/{self.social}</a>\n"
            + "</section>\n"
            + "</header>\n\n"
            + "---"
        )

    def __phone_fmt(self, number) -> str:
        return (
            number.replace("-", "")
            .replace("(", "")
            .replace(")", "")
            .replace(" ", "")
        )
