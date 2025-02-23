from sqlalchemy import Column, String, Integer, JSON
from app.database import Base


class Plant(Base):
    __tablename__ = "plants"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    species = Column(String, nullable=False)
    grow_guide = Column(
        JSON
    )  # Example: {"sunlight": "Full Sun", "soil": "Loamy", "watering": "Moderate"}
