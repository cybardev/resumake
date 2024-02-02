from dataclasses import dataclass

from ..utils import xp_fmt


@dataclass(kw_only=True)
class Education:
    school: str
    location: str
    program: str
    major: str
    start: str
    end: str
    courses: list[str]

    def __str__(self) -> str:
        return (
            xp_fmt(
                self.school,
                self.location,
                f"{self.program} in {self.major}",
                f"Graduation: {self.end}",
            )
            + "\n\n"
            + f"**Notable Courses**: "
            + ", ".join(self.courses)
        )
