#!/usr/bin/env python3

AUTHOR: str = "Sheikh Saad Abdullah"

RESUME_PARTS: dict[str, str] = {
    "header": "header.md",
    "education": "education.md",
    "skills": "skills.md",
    "projects": "projects.md",
    "experience": "experience.md",
}

SOURCE_DIR: str = "./src/"
OUTPUT_DIR: str = "./assets/"


class Resume:
    def __init__(self, parts: dict):
        self.data: dict[str, str] = {}

        # add sections in order
        for section, filename in parts.items():
            self.data[section] = self.__readfile(SOURCE_DIR + filename)

    def build(self, filename: str = f"Resume_{AUTHOR.replace(' ', '_')}.md"):
        with open(OUTPUT_DIR + filename, "w") as file:
            file.write(self.__str__())

    def __readfile(self, filename: str) -> str:
        result: str = ""
        with open(filename) as file:
            result = file.read()

        return result

    def __str__(self) -> str:
        return "\n".join(self.data.values()).strip()


if __name__ == "__main__":
    resume = Resume(RESUME_PARTS)
    resume.build()
