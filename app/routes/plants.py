from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.plant import PlantDatabase

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/{plant_id}")
async def get_plant(plant_id: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(PlantDatabase).where(PlantDatabase.id == plant_id))
    plant = result.scalars().first()

    if not plant:
        raise HTTPException(status_code=404, detail="Plant not found")

    return plant
