from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import get_db
from app.models.user import User
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me")
async def get_my_profile(
    db: AsyncSession = Depends(get_db), user: dict = Depends(get_current_user)
):
    result = await db.execute(select(User).where(User.id == user["sub"]))
    user_data = result.scalars().first()
    return user_data
