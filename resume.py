#!/usr/bin/env python3

from dataclasses import dataclass


def generate_resume(output_dir: str = "./assets/"):
    # instantiate an author object with default properties
    author: Person = default_author()

    # TODO: make any changes to author properties here
    author.projects.pop()
    author.projects.pop()
    author.experiences.pop()
    author.experiences.pop()
    author.skills[0].attributes.pop(0)

    # instantiate resume and output to file and standard output
    resume: Resume = Resume(author)
    resume.build(f"Resume_{author.name.replace(' ', '_')}.md", output_dir)
    print(resume)


def default_author():
    return Person(
        name="Sheikh Saad Abdullah",
        address=Address("2060 Quingate Place", "B3L 4P7"),
        phone="+1 (902) 818-0048",
        email="sheikh@cybar.dev",
        website="www.cybar.dev",
        social="cybardev",
        education=Education(
            school="Saint Mary's University",
            location="Halifax, Nova Scotia",
            program="Bachelor of Science",
            major="Computing Science",
            minor="Psychology",
            start="Sep 2020",
            end="Dec 2024",
            courses=[
                "Artificial Intelligence",
                "Data Structures and Algorithms",
                # "Operating Systems",
                "Software Engineering",
                "Systems Security",
            ],
        ),
        skills=[
            Skill(
                name="Skills",
                attributes=[
                    "Microsoft Office (Word, Excel, PowerPoint)",
                    "Python",
                    "HTML",
                    "CSS",
                    "Bootstrap",
                    "JavaScript",
                    "jQuery",
                    "ReactJS",
                    "NodeJS",
                    "ExpressJS",
                    "MongoDB",
                    "Java",
                    "C/C++",
                    "Git",
                ],
            ),
            Skill(
                name="Interests",
                attributes=[
                    "Linux",
                    "Open-source",
                    "Shell Scripting",
                    "Automation",
                    "Cloud",
                    "Front-end Web Development",
                    "Data Analytics",
                ],
            ),
        ],
        projects=[
            Project(
                name="yt.py - YouTube Media Player",
                address="https://github.com/cybardev/ytpy",
                role="Software Developer",
                start="Feb 2021",
                end="Present",
                attributes=[
                    'Translated the open-source shell script "ytfzf" into Python, improving cross-platform compatibility',
                    "Fetched YouTube search results by requesting resources via built-in Python modules, thus avoiding API calls, reducing dependencies, and simplifying end-user experience",
                    "Used a compiled regular expression to efficiently filter and gather media URL strings from raw JSON data retrieved",
                    "Ensured smooth media playback by delegating handling of media data to media player customizable by the user",
                ],
            ),
            Project(
                name="Cy | Pass - Secure Password Generator",
                address="https://pypi.org/project/cybarpass",
                role="Software Developer",
                start="Apr 2022",
                end="Present",
                attributes=[
                    "Modularized code by splitting up project into multiple scripts and using proper object-oriented techniques to ensure separation of concerns",
                    "Designed and implemented simple and elegant tkinter GUI and robust CLI for convenience and ease of access",
                    "Packaged and published project to Python Package Index (PyPI), making it easy and convenient for users to install",
                    "Created companion tool [CheckPass](https://checkpass.cybar.dev) to allow users to test the security of generated passphrase",
                ],
            ),
            Project(
                name="Cy | Search - Search Engine Frontend",
                address="https://search.cybar.dev",
                role="Full-stack Developer",
                start="Jan 2022",
                end="Apr 2022",
                attributes=[
                    "Designed a search engine frontend that uses NodeJS functions to request and fetch search results from a public API",
                    "Successfully displayed the fetched results in a clear and concise format",
                    "Secured the API key by encrypting it as a repository secret and using code obfuscation techniques",
                    "Implemented progressive web app functionality to allow users to install it as an app",
                ],
            ),
            Project(
                name="Accessible Blog with CMS",
                address="Northwood Care, Halifax, Nova Scotia",
                role="Full-stack Developer",
                start="Jan 2022",
                end="Apr 2022",
                attributes=[
                    "Collaborated with a team of 4 developers to create an accessible blog website with custom CMS and an on-screen keyboard for a client with cerebral palsy",
                    "Implemented both front-end and back-end using modern web technologies like Bootstrap, Alpine, Express, Mongo",
                    "Designed a workflow for continuous integration and deployment using GitHub Actions to automate releases",
                    "Successfully led the project's development and completion within 4 months, meeting all deadlines and specifications",
                ],
            ),
            Project(
                name="K'we - Mi'kmaq Language Learning Game",
                address="Eskasoni Immersion School, Eskasoni, Nova Scotia",
                role="Game Designer, Developer",
                start="Sep 2021",
                end="Jan 2022",
                attributes=[
                    "Collaborated with a team of 5 developers to design and develop an open-source educational video game for kids in grades 2-5, helping them learn the Mi'kmaq language",
                    "Successfully created engaging and age-appropriate content that was well-received by the target audience",
                    # "Built the game using the Free and Open-source Ren'Py game engine and hosted it on university servers using NodeJS",
                    "Enforced the Waterfall model of SDLC, ensuring high quality, thorough documentation, and debugging at every step",
                    "Managed the development process from start to finish, delivering the completed product within strict deadlines",
                ],
            ),
        ],
        experiences=[
            Experience(
                name="Sensor Technology LTD (COVE)",
                address="Dartmouth, Nova Scotia",
                role="Research Intern",
                start="May 2023",
                end="Aug 2023",
                attributes=[
                    "Configured Raspberry Pi SBCs with OpenPlotter Marine OS for the purpose of developing and testing the Acoustic Projector Control and Logging System",
                    "Developed Python script for generation and playback of audio files from given wavelength and duration",
                    "Implemented Python module to connect to private Signal K server and utilize its API to effectively retrieve sensor data",
                    "Created a script for logging data from sensors, consuming it via API calls, and storing it in an SQLite database",
                    # "Successfully set up Raspberry Pi units with OpenPlotter for testing and deployment of acoustic projectors",
                    # "Implemented a robust server-client API network, ensuring seamless communication between controller and logger units",
                    # "Developed a comprehensive database and logging system to efficiently store and retrieve data, facilitating data-driven decision-making",
                ],
            ),
            Experience(
                name="Saint Mary's University",
                address="Halifax, Nova Scotia",
                role="Computing Science Marker",
                start="Oct 2022",
                end="Apr 2023",
                attributes=[
                    "Tested and graded Java and Python code assignments submitted by students for performance and accuracy",
                    "Analyzed errors and suggested corrections to students as feedback",
                    "Successfully marked over 150 student assignments per semester",
                ],
            ),
            Experience(
                name="Saint Mary's University Students' Association",
                address="Halifax, Nova Scotia",
                role="Computer Science Tutor",
                start="Oct 2021",
                end="Sep 2022",
                attributes=[
                    "Tutored students in computing science fundamentals, increasing assigned coursework scores by over 40%",
                    "Helped achieve a better understanding of technical concepts and principles of web development in Python, Java, HTML, CSS, and JavaScript",
                ],
            ),
        ],
    )


def xp_fmt(name, address, spec, date):
    return (
        "<div class='xp-h'>"
        + f"<span>{name}</span>"
        + f"<span>{address}</span>"
        + "</div>\n"
        + "<div class='xp-s'>"
        + f"<span>{spec}</span>"
        + f"<span>{date}</span>"
        + "</div>"
    )


@dataclass
class Address:
    street: str
    postal_code: str
    city: str = "Halifax"
    province: str = "NS"
    province_full: str = "Nova Scotia"
    country: str = "Canada"

    def __str__(self) -> str:
        return f"{self.city}, {self.province}, {self.postal_code}"

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
            xp_fmt(
                self.school,
                self.location,
                f"{self.program} in {self.major}",
                f"Expected Graduation Date: {self.end}",
            )
            + "\n\n"
            + f"**Major Courses**: "
            + ", ".join(self.courses)
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
    address: str
    role: str
    start: str
    end: str
    attributes: list[str]

    def __str__(self):
        return (
            xp_fmt(
                self.name, self.address, self.role, f"{self.start} - {self.end}"
            )
            + "\n\n"
            + "\n".join([f"- {info}" for info in self.attributes])
        )


@dataclass(kw_only=True)
class Project(Experience):
    pass


@dataclass(kw_only=True)
class Person:
    name: str
    address: Address
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
            + f"<p>{str(self.address)}</p>\n"
            + "<section>\n"
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
                self.skills,
                self.experience,
                self.projects,
                self.education,
            ]
        )

    @property
    def header(self) -> str:
        return repr(self.author)

    @property
    def skills(self) -> str:
        return "## Skills & Interests\n\n" + "  \n".join(
            [str(skill) for skill in self.author.skills]
        )

    @property
    def projects(self) -> str:
        return "## Project Experience\n\n" + "\n\n".join(
            [str(project) for project in self.author.projects]
        )

    @property
    def experience(self) -> str:
        return "## Work Experience\n\n" + "\n\n".join(
            [str(experience) for experience in self.author.experiences]
        )

    @property
    def education(self) -> str:
        return f"## Education\n\n{self.author.education}"


if __name__ == "__main__":
    generate_resume()
