from datetime import date
from pydantic import BaseModel
from typing import Optional

class Mean_trade(BaseModel):
    user_id: int
    platform_id: int
    coin: str
    mean_buy: float
    mean_sell: float
    buy_minus_sell: float
    percent_gain_loss: float
