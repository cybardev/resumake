# initialize the resume module

# metadata
__version__ = "1.0.0"

# import everything needed for a resume
from resume.components.address import Address
from resume.components.author import Author
from resume.components.education import Education
from resume.components.experience import Experience
from resume.components.project import Project
from resume.components.resume import Resume
from resume.components.skill import Skill
from src.resume.utils import generate_resume
