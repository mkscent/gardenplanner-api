from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import DATABASE_URL

# Create async database engine
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# Async session factory
SessionLocal = sessionmaker(
    bind=engine, autoflush=False, autocommit=False, class_=AsyncSession
)

# Base class for SQLAlchemy models
Base = declarative_base()


# Dependency for getting DB session
async def get_db():
    async with SessionLocal() as session:
        yield session
