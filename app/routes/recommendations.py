from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.rotation import CropRotation

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/recommendations/{plant_id}")
async def get_recommendations(plant_id: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(CropRotation).where(CropRotation.plant_id == plant_id)
    )
    rotation_data = result.scalars().first()

    if not rotation_data:
        raise HTTPException(status_code=404, detail="No data available")

    return rotation_data
