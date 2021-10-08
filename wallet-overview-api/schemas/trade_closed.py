from datetime import date
from pydantic import BaseModel
from typing import Optional

class Trade_closed(BaseModel):
    user_id: int
    platform_id: int
    date: date
    timestamp: str
    type: str
    symbol: str
    received_currency: str
    received_quantity: float
    sent_currency: str
    sent_quantity: float
    fee_currency: str
    fee_quantity: float
    trade_value: float
    fee_value: float
    orderId: str
