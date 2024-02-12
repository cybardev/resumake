from dataclasses import dataclass


@dataclass(kw_only=True)
class Project:
    name: str
    url: str
    desc: str
    skills: list[str]

    def __str__(self) -> str:
        return f"**{self.name}** ({self.url}) {self.desc} **[{', '.join(self.skills)}]**"
