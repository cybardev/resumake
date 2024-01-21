from src.resume.components import *

# TODO: edit author object as required
author = Author(
    name="Sheikh Saad Abdullah",
    address=Address("2060 Quingate Place", "B3L 4P7"),
    phone="+1 (902) 818-0048",
    email="sheikh@cybar.dev",
    website="www.cybar.dev",
    social="cybardev",
    skills=[
        Skill(
            name="Skills",
            attributes=[
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
                "DevOps",
                "Agile Development",
                "Data Analytics",
            ],
        ),
    ],
    experiences=[
        Experience(
            name="ReelData AI",
            address="Halifax, Nova Scotia",
            role="Junior Software Developer",
            start="Sept 2023",
            end="Dec 2023",
            attributes=[
                "Collaborated with a dynamic Agile team on ReelAppetite, a key product, demonstrating strong teamwork and interpersonal skills",
                "Successfully integrated into a large existing codebase, showcasing adaptability and quick learning",
                "Implemented features using test-driven development and containerization, contributing to the software's robustness",
                "Experienced the deployment of code to production, highlighting practical application and impact of contributions",
            ],
        ),
        Experience(
            name="Sensor Technology LTD (COVE)",
            address="Dartmouth, Nova Scotia",
            role="Research Intern",
            start="May 2023",
            end="Aug 2023",
            attributes=[
                "Configured Raspberry Pi SBCs with OpenPlotter Marine OS for the purpose of developing and testing the Acoustic Projector Control and Logging System",
                "Developed Python script for generation and playback of audio files from given wavelength and duration",
                "Implemented module to connect to private Signal K server and utilize its API to effectively retrieve sensor data",
                "Created a script for logging data from sensors, consuming it via API calls, and storing it in an SQLite database",
            ],
        ),
    ],
    projects=[
        Project(
            name="Cy | Pass - Secure Password Generator",
            address="https://pypi.org/project/cybarpass",
            role="Software Developer",
            start="Apr 2022",
            end="Apr 2023",
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
    ],
    education=Education(
        school="Saint Mary's University",
        location="Halifax, Nova Scotia",
        program="Bachelor of Science",
        major="Computing Science",
        start="Sep 2020",
        end="Dec 2024",
        courses=[
            "Artificial Intelligence",
            "Data Structures and Algorithms",
            "Software Engineering",
            "Systems Security",
        ],
    ),
)
