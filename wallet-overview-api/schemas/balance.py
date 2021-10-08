from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class Balance(BaseModel):
    user_id: int
    platform_id: int
    coin: str
    quantity_free: float
    quantity_locked: float
    quantity_total: float
    value: float
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
