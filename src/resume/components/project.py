from dataclasses import dataclass

from src.resume.components.experience import Experience


@dataclass(kw_only=True)
class Project(Experience):
    pass
