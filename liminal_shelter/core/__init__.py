"""
Core modules for Liminal Shelter

Contains the fundamental classes:
- GuardianCore: The parental AI model that creates and protects
- SeedlingModel: The vulnerable child AI model that learns and grows
- LiminalShelter: The protected space where growth happens safely
"""

from .guardian import GuardianCore
from .seedling import SeedlingModel
from .shelter import LiminalShelter

__all__ = ["GuardianCore", "SeedlingModel", "LiminalShelter"]
