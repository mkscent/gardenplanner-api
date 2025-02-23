from sqlalchemy import Column, String, JSON
from app.database import Base


class CropRotation(Base):
    __tablename__ = "crop_rotation"

    id = Column(String, primary_key=True, index=True)
    plant_id = Column(String, nullable=False)
    bad_following_plants = Column(
        JSON
    )  # Example: {"potatoes": ["tomatoes", "peppers"]}
    good_companions = Column(JSON)  # Example: {"tomatoes": ["basil", "marigold"]}
