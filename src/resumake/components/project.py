from dataclasses import dataclass

from ..utils import url_fmt
from .experience import Experience


class Project(Experience):
    def __init__(
        self,
        name: str,
        url: str,
        role: str,
        start: str,
        end: str,
        attributes: list[str],
    ):
        super().__init__(
            name=name,
            address=url_fmt(url),
            role=role,
            start=start,
            end=end,
            attributes=attributes,
        )


@dataclass(kw_only=True)
class ProjectSummary:
    name: str
    url: str
    desc: str
    skills: list[str]

    def __str__(self) -> str:
        return f"**{self.name}** ({url_fmt(self.url)}) {self.desc} **[{', '.join(self.skills)}]**"
