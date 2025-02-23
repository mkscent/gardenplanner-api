from fastapi import Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError

from app.utils.jwt import verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def get_current_user(token: str = Security(oauth2_scheme)):
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    return payload  # Contains user ID
