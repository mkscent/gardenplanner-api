import uuid
from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.dependencies.auth import get_current_user
from app.models.journal import Journal

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
async def add_journal_entry(
    garden_id: str,
    note: str,
    db: AsyncSession = Depends(get_db),
    user: dict = Depends(get_current_user),
):
    new_entry = Journal(
        id=str(uuid.uuid4()),
        user_id=user["id"],
        garden_id=garden_id,
        notes=[{"date": str(datetime.now()), "note": note}],
    )

    db.add(new_entry)
    await db.commit()
    await db.refresh(new_entry)
    return new_entry
