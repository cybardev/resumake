from dataclasses import dataclass


@dataclass(kw_only=True)
class Skill:
    name: str
    attributes: list[str]

    def __str__(self):
        return f"**{self.name}**: " + ", ".join(self.attributes)
