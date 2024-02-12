from fastapi import APIRouter
from fastapi import HTTPException
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

@router.get("/grimoire/")
async def grimoire_welcome():
    return "Grimoire of the Gardening Arts!"

class Init(BaseModel):
    plant: str
    zipcode: int
    start: datetime
    comments: str

@router.post("/grimoire/new_route")
async def new_route(item: Init):
    if not item.value1 or not item.value2 or not item.value3:
        raise HTTPException(status_code=400, detail="Invalid input")
    return {"value1": item.value1, "value2": item.value2, "value3": item.value3}

# Idea behind this will be to step through a clietn config, setting the zip and time
# LLM responds with a structured response of plants you could grow in that area
# Back anf forth helps user build a custom tailored garden plan
# Client can handle errors by alerting the backend to a data it cannot parse into UI,
# and LLM can respond with another attempt at the correct structured response. 