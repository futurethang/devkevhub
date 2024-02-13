# models.py or schemas/initial_data.py

from pydantic import BaseModel
from datetime import datetime

class InitialData(BaseModel):
    plant: str
    zipcode: int
    start: datetime
    comments: str
