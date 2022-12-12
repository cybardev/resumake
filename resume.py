#!/usr/bin/env python3

from dataclasses import dataclass


def generate_resume(output_dir: str = "./assets/"):
    # instantiate an author object with default properties
    author: Person = default_author()

    # TODO: make any changes to author properties here

    # instantiate resume and output to file and standard output
    resume: Resume = Resume(author)
    resume.build(f"Resume_{author.name.replace(' ', '_')}.md", output_dir)
    print(resume)


def default_author():
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
            Project(
                name="Cy | Search - Search Engine Frontend",
                start="Jan 2022",
                end="Apr 2022",
                address="https://search.cybar.dev",
                attributes=[
                    "Designed a search engine frontend with minimalistic aesthetics to ensure clarity",
                    "Utilized NodeJS calls to request and fetch search results from API endpoints",
                    "Displayed results to user using modern web technologies such as Bootstrap, AlpineJS",
                    "Obfuscated API keys using repository secrets to prevent leaking and misuse",
                ],
            ),
            Project(
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
            Project(
                name="K'we - Mi'kmaq Language Learning Game",
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


class Address:
    street: str
    postal_code: str
    city: str = "Halifax"
    province: str = "NS"
    province_full: str = "Nova Scotia"
    country: str = "Canada"

    def __str__(self) -> str:
        return f"{self.city}, {self.province} {self.postal_code}"

    def __repr__(self) -> str:
        return f"{self.street}, {self}"


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

    def __str__(self) -> str:
        return (
            f"**{self.program}** ({self.start} - {self.end})  \n"
            + f"**{self.school}**, {self.location}  \n"
            + f"**Major**: {self.major}, **Minor**: {self.minor}  \n"
            + f"**Courses**: "
            + ",".join(self.courses)
            + ", etc."
        )


@dataclass(kw_only=True)
class Skill:
    name: str
    attributes: list[str]

    def __str__(self):
        return f"**{self.name}**: " + ", ".join(self.attributes)


@dataclass(kw_only=True)
class Experience:
    name: str
    start: str
    end: str
    address: str
    attributes: list[str]

    def __str__(self):
        return (
            f"**{self.name}** ({self.start} - {self.end})  \n"
            + f"_{self.address}_  \n\n"
            + "\n".join([f"- {info}" for info in self.attributes])
        )


@dataclass(kw_only=True)
class Project(Experience):
    pass


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
    projects: list[Project]
    experiences: list[Experience]

    def __repr__(self):
        return (
            f"# {self.name}\n\n"
            + "<header>\n"
            + f"<p>{self.address}</p>\n"
            + "<section style='display: flex; justify-content: space-around; margin-top: 1.1em;'>\n"
            + f"<a href='tel:{self.__phone_fmt(self.phone)}'>{self.phone}</a>\n"
            + f"<a href='mailto:{self.email}'>{self.email}</a>\n"
            + f"<a href='https://{self.website}'>{self.website}</a>\n"
            + f"<a href='https://github.com/{self.social}'>github.com/{self.social}</a>\n"
            + f"<a href='https://www.linkedin.com/in/{self.social}'>linkedin.com/in/{self.social}</a>\n"
            + "</section>\n"
            + "</header>\n\n"
            + "---"
        )

    def __phone_fmt(self, number) -> str:
        return (
            number.replace("-", "")
            .replace("(", "")
            .replace(")", "")
            .replace(" ", "")
        )


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
                self.projects,
                self.experience,
                self.skills,
            ]
        )

    @property
    def header(self) -> str:
        return repr(self.author)

    @property
    def education(self) -> str:
        return "## <u>Education</u>\n\n" + str(self.author.education)

    @property
    def skills(self) -> str:
        return "## <u>Technical Skills</u>\n\n" + "  \n".join(
            [str(skill) for skill in self.author.skills]
        )

    @property
    def projects(self) -> str:
        return "## <u>Projects</u>\n\n" + "\n\n".join(
            [str(project) for project in self.author.projects]
        )

    @property
    def experience(self) -> str:
        return "## <u>Experience</u>\n\n" + "\n\n".join(
            [str(experience) for experience in self.author.experiences]
        )


if __name__ == "__main__":
    generate_resume()
