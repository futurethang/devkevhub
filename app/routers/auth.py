from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.utils import create_access_token
from datetime import timedelta

ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter()

def authenticate_user(username: str, password: str):
    # // Here, you should verify the username and password, e.g., against a database
    # // For simplicity, let's assume the user is authenticated
    user = {"username": username, "password": password}  # // This should be your actual user model or dictionary
    if not user:
        return False
    return user

@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
