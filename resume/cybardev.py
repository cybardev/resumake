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
                "Collaborated with a dynamic remote-first Agile team on ReelAppetite - a flagship product - implementing key features according to client requirements, boosting client satisfaction and trust",
                "Implemented features using test-driven development by creating unit tests and containerized integration tests to be run in the CI/CD pipeline, contributing to the software's robustness and preventing bugs from reaching production",
                "Developed Python module to annotate videos with metadata consumed from Apache Kafka topics using GStreamer pipelines, allowing farm operators to view video stream information via dashboard",
            ],
        ),
        Experience(
            name="Sensor Technology LTD (COVE)",
            address="Dartmouth, Nova Scotia",
            role="Research Intern",
            start="May 2023",
            end="Aug 2023",
            attributes=[
                "Configured Raspberry Pi SBCs with Linux to develop and test the Acoustic Projector Control and Logging System",
                "Developed Python script for generation and playback of audio files from given wavelength and duration",
                "Implemented module to connect to private Signal K server and utilize its API to effectively retrieve sensor data",
                "Created a script for logging data from sensors, consuming it via API calls, and storing it in an SQLite database",
            ],
        ),
        # ExperienceSummary(
        #     name="The Source (BELL)",
        #     role="Seasonal Sales Associate",
        #     start="Oct 2022",
        #     end="Dec 2022",
        #     desc="Assisted customers with finding the best electronic products for their purposes. Utilized effective marketing and communication techniques to promote products and services.",
        #     skills=["Marketing", "Sales", "Customer Service", "Communication"],
        # ),
    ],
    projects=[
        # Project(
        #     name="Resumake - Programmatic Resume Generator",
        #     url="github.com/cybardev/resumake",
        #     role="Software Developer",
        #     start="Jun 2022",
        #     end="Present",
        #     attributes=[
        #         "Modularized code by splitting up project into multiple component files and using proper object-oriented techniques to ensure separation of concerns",
        #         "Containerized application in a Docker image via Dockerfile configuration to create self-contained package with proper dependency resolution",
        #         "Packaged and published project to Python Package Index (PyPI), DockerHub, and GitHub Packages registries, making it easy and convenient for users to install",
        #         "Created GitHub Actions workflows for CI/CD, to automatically build and deploy to package registries on tagged pushes, as well as re-generating personal resume and publishing to static website (https://resume.cybar.dev)",
        #     ],
        # ),
        ProjectSummary(
            name="Resumake",
            url="github.com/cybardev/resumake",
            desc="Programmatic resume generator published to PyPI and DockerHub, built and deployed using GitHub Actions CI/CD workflow for easy installation and usage.",
            skills=["Python", "Docker", "CI/CD"],
        ),
        ProjectSummary(
            name="CybarPass",
            url="github.com/cybardev/CybarPass",
            desc="Secure passphrase generator with GUI and CLI, published to PyPI. Companion webapp CheckPass can be used to check security of passphrases.",
            skills=["Python", "Cybersecurity", "GUI Development"],
        ),
        ProjectSummary(
            name="Prayers",
            url="github.com/cybardev/prayers",
            desc="API to retrieve Islamic prayer time for a given location and date. Uses serverless functions on the cloud for reliable persistent service.",
            skills=["JavaScript", "API Development", "Serverless Functions"],
        ),
        ProjectSummary(
            name="Accessible Blog",
            url="github.com/cybardev/blog",
            desc="Full-stack webapp with custom CMS and accessible on-screen keyboard made for client with Cerebral Palsy. Group project as part of university course.",
            skills=["JavaScript", "MongoDB", "ExpressJS"],
        ),
        ProjectSummary(
            name="yt.py",
            url="github.com/cybardev/ytpy",
            desc="YouTube media player that uses web scraping techniques to play media from YouTube without the YouTube API. Also translated to Go (github.com/cybardev/ytgo)",
            skills=["Python", "Go", "Web Scraping", "CLI Development"],
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
            name="Technologies",
            attributes=[
                "Python",
                "HTML",
                "CSS",
                "Bootstrap",
                "JavaScript",
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
