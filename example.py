#!/usr/bin/env python3


from src.resume import *


me: Author = Author(
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
                "Front-end Web Development",
                "Data Analytics",
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


if __name__ == "__main__":
    generate_resume(me, "./assets/")
