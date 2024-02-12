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
    ],
    projects=[
        Project(
            name="Resumake",
            url="github.com/cybardev/resumake",
            desc="Programmatic resume generator published to PyPI and DockerHub, built and deployed using GitHub Actions CI/CD workflow for easy installation and usage.",
            skills=["Python", "Docker", "CI/CD"],
        ),
        Project(
            name="CybarPass",
            url="github.com/cybardev/CybarPass",
            desc="Secure passphrase generator with GUI and CLI, published to PyPI. Companion webapp CheckPass can be used to check security of passphrases.",
            skills=["Python", "Cybersecurity", "GUI Development"],
        ),
        Project(
            name="Prayers",
            url="github.com/cybardev/prayers",
            desc="API to retrieve Islamic prayer time for a given location and date. Uses serverless functions on the cloud for persistent service.",
            skills=["JavaScript", "API Development", "Serverless Functions"],
        ),
        Project(
            name="Accessible Blog",
            url="github.com/cybardev/blog",
            desc="Full-stack webapp with custom CMS and accessible on-screen keyboard made for client with Cerebral Palsy. Group project as part of university course.",
            skills=["JavaScript", "MongoDB", "ExpressJS"],
        ),
        Project(
            name="yt.py",
            url="github.com/cybardev/ytpy",
            desc="YouTube media player that uses web scraping techniques to retrieve and play media from YouTube without using the YouTube API.",
            skills=["Python", "Web Scraping", "CLI Development"],
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
