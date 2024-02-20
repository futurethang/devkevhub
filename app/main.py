from fastapi import FastAPI, APIRouter 
from app.routers import items, users, grimoire, auth_test, auth

app = FastAPI()
v1_router = APIRouter(prefix="/v1")

v1_router.include_router(items.router)
v1_router.include_router(users.router)
v1_router.include_router(grimoire.router)
v1_router.include_router(auth_test.router)
v1_router.include_router(auth.router)

app.include_router(v1_router)