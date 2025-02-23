from sqlalchemy import Column, String, JSON, ForeignKey
from app.database import Base


class Garden(Base):
    __tablename__ = "gardens"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"))
    name = Column(String, nullable=False)
    size = Column(JSON)  # Example: {"width": 10, "height": 5}
    layout = Column(JSON)  # Example: {"plants": [{"id": "plant1", "x": 2, "y": 3}]}
