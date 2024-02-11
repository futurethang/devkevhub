from fastapi import APIRouter

router = APIRouter()

@router.get("/users/")
async def read_items():
    return [{"name": "Doug"}, {"name": "Sally"}]
