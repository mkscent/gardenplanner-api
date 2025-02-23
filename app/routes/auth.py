from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import uuid

from app.models.user import User
from app.database import get_db
from app.utils.security import hash_password, verify_password
from app.utils.jwt import create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register")
async def register(email: str, password: str, db: AsyncSession = Depends(get_db)):
    # Check if user exists
    result = await db.execute(select(User).where(User.email == email))
    existing_user = result.scalars().first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        id=str(uuid.uuid4()), email=email, hashed_password=hash_password(password)
    )

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return {"message": "User registered successfully"}


@router.post("/login")
async def login(email: str, password: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalars().first()

    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token({"sub": user.id})
    return {"access_token": access_token, "token_type": "bearer"}
