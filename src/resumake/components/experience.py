from dataclasses import dataclass

from ..utils import xp_fmt


@dataclass(kw_only=True)
class Experience:
    name: str
    address: str
    role: str
    start: str
    end: str
    attributes: list[str]

    def __str__(self):
        return (
            xp_fmt(
                self.name, self.address, self.role, f"{self.start} - {self.end}"
            )
            + "\n\n"
            + "\n".join([f"- {info}" for info in self.attributes])
        )


@dataclass(kw_only=True)
class ExperienceSummary:
    name: str
    role: str
    start: str
    end: str
    desc: str
    skills: list[str]

    def __post_init__(self):
        self.position = f"{self.role}, _{self.start} - {self.end}_"

    def __str__(self) -> str:
        return f"**{self.name}** ({self.position}) {self.desc} **[{', '.join(self.skills)}]**"
