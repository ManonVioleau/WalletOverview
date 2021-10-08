from datetime import date
from pydantic import BaseModel
from typing import Optional

class Transfert_ordered(BaseModel):
    user_id: int
    platform_id: int
    date: date
    timestamp: str
    value: float