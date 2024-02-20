from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter()

@router.get("/items/")
async def read_items():
    return [{"name": "Item Foo"}, {"name": "Item Bar"}]

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=[os.getenv("ALGORITHM")])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        # // Here you should return the user object based on username
        # // This example assumes a simple verification
        user = {"username": username, "butt": "fart"}
        return user
    except JWTError:
        raise credentials_exception

@router.get("/protected-route")
async def read_protected_route(current_user: dict = Depends(get_current_user)):
    return {"user": current_user}
