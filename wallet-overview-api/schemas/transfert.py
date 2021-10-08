from datetime import date
from pydantic import BaseModel
from typing import Optional

class Transfert(BaseModel):
    user_id: int
    platform_id: int
    date: date
    timestamp: str
    type: str
    coin: str
    quantity: float
    fees: float
    transfert_value: float
    fee_value: float
    network: str
    address: str
    status: str
    dep_with_value: float