# initialize the resume module

# metadata
__version__ = "1.0.0"

# import everything needed for a resume
from src.resume.components.address import Address
from src.resume.components.author import Author
from src.resume.components.education import Education
from src.resume.components.experience import Experience
from src.resume.components.project import Project
from src.resume.components.resume import Resume
from src.resume.components.skill import Skill
from src.resume.utils import generate_resume
