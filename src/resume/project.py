from dataclasses import dataclass

from src.resume.experience import Experience


@dataclass(kw_only=True)
class Project(Experience):
    pass
