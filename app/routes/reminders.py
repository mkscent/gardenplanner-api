import uuid
from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.dependencies.auth import get_current_user
from app.services.email_service import send_email

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
async def create_reminder(
    plant_id: str,
    remind_at: datetime,
    db: AsyncSession = Depends(get_db),
    user: dict = Depends(get_current_user),
):
    # new_reminder = Reminder(id=str(uuid.uuid4()), user_id=user["id"], plant_id=plant_id, remind_at=remind_at)
    #
    # db.add(new_reminder)
    # await db.commit()
    # await db.refresh(new_reminder)
    #
    # await send_email(user["email"], "Gardening Reminder", f"Time to take care of {plant_id}!")
    # return new_reminder
    ...
