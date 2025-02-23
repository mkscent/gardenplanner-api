import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.dependencies.auth import get_current_user
from app.models.garden import Garden
from app.schemas.garden import GardenResponse

router = APIRouter(prefix="/gardens", tags=["Gardens"])


@router.post("/", response_model=GardenResponse)
async def create_garden(
    name: str,
    size: dict,
    layout: dict,
    db: AsyncSession = Depends(get_db),
    user: dict = Depends(get_current_user),
):
    new_garden = Garden(
        id=str(uuid.uuid4()), user_id=user["id"], name=name, size=size, layout=layout
    )

    db.add(new_garden)
    await db.commit()
    await db.refresh(new_garden)
    return new_garden


@router.post("/follow-on/{garden_id}")
async def generate_follow_on_plan(
    garden_id: str,
    db: AsyncSession = Depends(get_db),
    user: dict = Depends(get_current_user),
):
    result = await db.execute(select(Garden).where(Garden.id == garden_id))
    old_garden = result.scalars().first()

    if not old_garden:
        raise HTTPException(status_code=404, detail="Garden not found")

    new_garden = Garden(
        id=str(uuid.uuid4()),
        user_id=user["id"],
        name=f"{old_garden.name} (Next Year)",
        size=old_garden.size,
        layout=old_garden.layout,
    )

    db.add(new_garden)
    await db.commit()
    await db.refresh(new_garden)
    return new_garden
