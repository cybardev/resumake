#!/usr/bin/env python3

from dataclasses import dataclass

PATH: str = "./"


def generate_resume(output_dir: str = PATH + "assets/"):
    # instantiate an author object with default properties
    author: Person = default_author()

    # TODO: make any changes to author properties here

    # instantiate resume and output to file and standard output
    resume: Resume = Resume(author)
    resume.build(f"Resume_{author.name.replace(' ', '_')}.md", output_dir)
    print(resume)


@dataclass(kw_only=True)
class Education:
    school: str
    location: str
    program: str
    major: str
    minor: str
    start: str
    end: str
    courses: list[str]


@dataclass(kw_only=True)
class Skill:
    name: str
    attributes: list[str]


@dataclass(kw_only=True)
class Experience:
    name: str
    start: str
    end: str
    address: str
    attributes: list[str]


@dataclass(kw_only=True)
class Person:
    name: str
    address: str
    phone: str
    email: str
    website: str
    social: str
    education: Education
    skills: list[Skill]
    projects: list[Experience]
    experiences: list[Experience]


class Resume:
    def __init__(self, author: Person):
        self.author = author

    def build(self, filename: str, output_dir: str):
        with open(output_dir + filename, "w") as file:
            file.write(str(self))

    def __str__(self) -> str:
        return "\n\n".join(
            [
                self.header,
                self.education,
                self.skills,
                self.projects,
                self.experience,
            ]
        )

    @property
    def header(self) -> str:
        auth: Person = self.author

        return (
            f"# {auth.name}\n\n"
            + "<header>\n"
            + f"<p>{auth.address}</p>\n"
            + "<section style='display: flex; justify-content: space-around; margin-top: 1.1em;'>\n"
            + f"<a href='tel:{self.__phone_format(auth.phone)}'>{auth.phone}</a>\n"
            + f"<a href='mailto:{auth.email}'>{auth.email}</a>\n"
            + f"<a href='https://{auth.website}'>{auth.website}</a>\n"
            + f"<a href='https://github.com/{auth.social}'>github.com/{auth.social}</a>\n"
            + f"<a href='https://www.linkedin.com/in/{auth.social}'>linkedin.com/in/{auth.social}</a>\n"
            + "</section>\n"
            + "</header>\n\n"
            + "---"
        )

    @property
    def education(self) -> str:
        edu: Education = self.author.education

        return (
            "## <u>Education</u>\n\n"
            + f"**{edu.program}** ({edu.start} - {edu.end})  \n"
            + f"**{edu.school}**, {edu.location}  \n"
            + f"**Major**: {edu.major}, **Minor**: {edu.minor}  \n"
            + f"**Courses**: "
            + ",".join(edu.courses)
            + ", etc."
        )

    @property
    def skills(self) -> str:
        res: str = "## <u>Technical Skills</u>\n\n"

        for skill in self.author.skills:
            res += f"**{skill.name}**: " + ", ".join(skill.attributes) + "\n\n"

        return res.strip()

    @property
    def projects(self) -> str:
        res: str = "## <u>Projects</u>\n\n"

        for project in self.author.projects:
            res += (
                f"**{project.name}** ({project.start} - {project.end})  \n"
                + f"_{project.address}_  \n\n"
            )
            for info in project.attributes:
                res += f"- {info}\n"
            res += "\n"

        return res.strip()

    @property
    def experience(self) -> str:
        res: str = "## <u>Experience</u>\n\n"

        for experience in self.author.experiences:
            res += (
                f"**{experience.name}** ({experience.start} - {experience.end})  \n"
                + f"_{experience.address}_  \n\n"
            )
            for info in experience.attributes:
                res += f"- {info}\n"
            res += "\n"

        return res.strip()

    def __phone_format(self, number) -> str:
        return (
            number.replace("-", "")
            .replace("(", "")
            .replace(")", "")
            .replace(" ", "")
        )


def default_author() -> Person:
    return Person(
        name="Sheikh Saad Abdullah",
        address="Halifax, Nova Scotia B3J 2K9",
        phone="+1 (902) 818-0048",
        email="sheikh@cybar.dev",
        website="www.cybar.dev",
        social="cybardev",
        education=Education(
            school="Saint Mary's University",
            location="Halifax, Nova Scotia",
            program="Bachelor of Science (B.Sc.) with Co-op",
            major="Computing Science",
            minor="Psychology",
            start="Sep 2020",
            end="Dec 2024",
            courses=[
                "Software Engineering",
                "Mobile App Development",
                "Data Structure and Algorithms",
            ],
        ),
        skills=[
            Skill(
                name="Programming Languages",
                attributes=[
                    "Python",
                    "Shell Script",
                    "HTML",
                    "CSS",
                    "JavaScript",
                    "Java",
                    "C",
                    "C++",
                ],
            ),
            Skill(
                name="Technologies",
                attributes=[
                    "Microsoft Office (Word, Excel, PowerPoint)",
                    "Linux",
                    "Git",
                    "jQuery",
                    "Bootstrap",
                ],
            ),
        ],
        projects=[
            Experience(
                name="Cy | Search - Search Engine Frontend",
                start="Jan 2022",
                end="Apr 2022",
                address="https://search.cybar.dev",
                attributes=[""],
            ),
            Experience(
                name="Accessible Blog with CMS",
                start="Jan 2022",
                end="Apr 2022",
                address="Northwood Care, Halifax, Nova Scotia",
                attributes=[
                    "Served as the project manager in a team of 4 peers for our Mobile App Development course",
                    "Designed a workflow for continuous integration and deployment using GitHub Actions to automate releases",
                    "Built a 3-page blog website as well as a custom CMS (content management system) admin page",
                    "Created an accessible on-screen keyboard to accommodate client's typing difficulties caused by Cerebral Palsy",
                    "Implemented the blog as a full-stack webapp using Bootstrap, jQuery, AlpineJS, Node, Express, and MongoDB",
                    "Enforced CRUD standards to efficiently handle database operations",
                ],
            ),
            Experience(
                name="K'we - Language Learning Game",
                start="Sep 2021",
                end="Jan 2022",
                address="Eskasoni Immersion School, Halifax, Nova Scotia",
                attributes=[
                    "Teamed up with 5 peers as part of our Software Engineering course",
                    "Managed the codebase in an organizational GitHub repository created for the project for continuous integration",
                    "Built a game using Ren'Py and Unity that children from grades 2 to 5 played at school",
                    "Enhanced the children's experience with learning the Mi'kmaq language",
                ],
            ),
        ],
        experiences=[
            Experience(
                name="Computer Science Tutor",
                start="Oct 2021",
                end="Sep 2022",
                address="Halifax, Nova Scotia",
                attributes=[
                    "Explained fundamentals of programming and web development in Python, Java, HTML, CSS, JavaScript, SQL, etc.",
                    "Assisted in understanding core technical concepts and web development principles",
                    "Helped achieve an increase of over 40% in assigned coursework scores",
                ],
            )
        ],
    )


if __name__ == "__main__":
    generate_resume()
