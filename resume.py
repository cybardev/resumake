#!/usr/bin/env python3

AUTHOR: str = "Sheikh Saad Abdullah"

RESUME_PARTS: dict[str, str] = {
    "header": "header.md",
    "education": "education.md",
    "skills": "skills.md",
    "projects": "projects.md",
    "experience": "experience.md",
}

PATH: str = "./"
SOURCE_DIR: str = PATH + "src/"
OUTPUT_DIR: str = PATH + "assets/"


class Resume:
    def __init__(self, parts: dict):
        # add sections in order
        self.data: dict[str, str] = {}
        for section, filename in parts.items():
            with open(SOURCE_DIR + filename) as file:
                self.data[section] = file.read()

    def build(self, filename: str = f"Resume_{AUTHOR.replace(' ', '_')}.md"):
        with open(OUTPUT_DIR + filename, "w") as file:
            file.write(self.__str__())

    def __str__(self) -> str:
        return "\n".join(self.data.values()).strip()


if __name__ == "__main__":
    resume = Resume(RESUME_PARTS)
    resume.build()
