from dataclasses import dataclass


@dataclass(kw_only=True)
class Project:
    name: str
    url: str
    desc: str
    skills: list[str]

    def __str__(self) -> str:
        skills = ", ".join((f"`{skill}`" for skill in self.skills))
        return f"**{self.name}** _({self.url})_ {self.desc} [{skills}]"
