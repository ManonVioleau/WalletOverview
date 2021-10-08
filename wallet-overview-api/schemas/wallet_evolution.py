from datetime import date
from pydantic import BaseModel
from typing import Optional

class Wallet_evolution(BaseModel):
    user_id: int
    platform_id: int
    date: date
    timestamp: str
    wallet_value_BTC: float
    wallet_value_USDT: float
