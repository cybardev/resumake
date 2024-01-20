from dataclasses import dataclass

from .experience import Experience


@dataclass(kw_only=True)
class Project(Experience):
    pass
