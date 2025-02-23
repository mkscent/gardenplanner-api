from pydantic import BaseModel
from typing import Dict, Optional
import uuid


class GardenBase(BaseModel):
    name: str
    size: Dict[str, float]  # Example: {"width": 10, "height": 15}
    layout: Dict[str, str]  # Example: {"section1": "Tomatoes", "section2": "Carrots"}


class GardenCreate(GardenBase):
    pass  # Used for creation (inherits from GardenBase)


class GardenResponse(GardenBase):
    id: uuid.UUID
    user_id: uuid.UUID

    class Config:
        from_attributes = True  # Needed to work with SQLAlchemy models
