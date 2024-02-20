from fastapi import FastAPI
from app.routers import items, users, grimoire, auth_test, auth

app = FastAPI()

app.include_router(items.router)
app.include_router(users.router)
app.include_router(grimoire.router)
app.include_router(auth_test.router)
app.include_router(auth.router)