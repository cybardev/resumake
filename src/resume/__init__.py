# initialize the resume module

# metadata
__version__ = "1.0.0"

# import everything needed for a resume
from .components.address import Address
from .components.author import Author
from .components.education import Education
from .components.experience import Experience
from .components.project import Project
from .components.resume import Resume
from .components.skill import Skill
from .utils import generate_resume, md_to_pdf
