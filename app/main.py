from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.database import engine, Base
import uvicorn

# Import routes
from app.routes.auth import router as auth_router
from app.routes.users import router as user_router
from app.routes.gardens import router as garden_router

# Lifespan event for startup/shutdown


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)  # Creates tables
    yield
    await engine.dispose()  # Cleanup on shutdown


# Initialize FastAPI app
app = FastAPI(title="Gardening App API", version="1.0", lifespan=lifespan)

# CORS Middleware (Allow frontend to access API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Routes
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(garden_router)

# Run the server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
