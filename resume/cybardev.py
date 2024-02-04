from resumake.components import *

author = Author(
    name="Sheikh Saad Abdullah",
    address=Address("2060 Quingate Place", "B3L 4P7"),
    phone="+1 (902) 818-0048",
    email="sheikh@cybar.dev",
    website="www.cybar.dev",
    social="cybardev",
    profile="Adaptable and enthusiastic Computer Science major with expertise in Python, JavaScript, Git, Linux, and various standard tools and technologies. "
    + "Completed two co-op internships in the software development industry and proactively engaged in creating open-source software projects, "
    + "showcasing a commitment to continuous learning and creative problem-solving. Highly interested in DevOps and Cloud computing, "
    + "currently preparing for the AWS Cloud Practitioner certification exam.",
    experiences=[
        Experience(
            name="ReelData AI",
            address="Halifax, Nova Scotia",
            role="Junior Software Developer",
            start="Sept 2023",
            end="Dec 2023",
            attributes=[
                "Collaborated with a dynamic Agile team on ReelAppetite - a flagship product - implementing key features according to client requirements, demonstrating strong teamwork and interpersonal skills",
                "Successfully integrated into a large existing codebase, showcasing adaptability and quick learning",
                "Implemented features using test-driven development and containerization, contributing to the software's robustness",
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
            name="Resumake - Programmatic Resume Generator",
            address="https://github.com/cybardev/resumake",
            role="Software Developer",
            start="Jun 2022",
            end="Present",
            attributes=[
                "Modularized code by splitting up project into multiple component files and using proper object-oriented techniques to ensure separation of concerns",
                "Containerized application in a Docker image via Dockerfile configuration to create self-contained package with proper dependency resolution",
                "Packaged and published project to Python Package Index (PyPI), DockerHub, and GitHub Packages registries, making it easy and convenient for users to install",
                "Created GitHub Actions workflows for CI/CD, to automatically build and deploy to package registries on tagged pushes, as well as re-generating personal resume and publishing to static website (https://resume.cybar.dev)",
            ],
        ),
    ],
    education=Education(
        school="Saint Mary's University",
        location="Halifax, Nova Scotia",
        program="Bachelor of Science",
        major="Computing Science",
        start="Sep 2020",
        end="Jan 2025",
        courses=[
            "Artificial Intelligence",
            "Data Structures and Algorithms",
            "Software Engineering",
            "Systems Security",
        ],
    ),
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
                "CI/CD",
                "DevOps",
                "Agile Development",
                "Data Analytics",
            ],
        ),
    ],
)
