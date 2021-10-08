from datetime import date
from pydantic import BaseModel
from typing import Optional

class Trade_open(BaseModel):
    user_id: int
    platform_id: int
    date: date
    timestamp: str
    type: str
    symbol: str
    quantity: float
    price: float