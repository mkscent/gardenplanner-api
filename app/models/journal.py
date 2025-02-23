from sqlalchemy import Column, String, JSON, ForeignKey
from app.database import Base


class Journal(Base):
    __tablename__ = "journal"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"))
    garden_id = Column(String, ForeignKey("gardens.id"))
    notes = Column(JSON)  # Example: [{"date": "2024-02-01", "note": "First sprouts!"}]
