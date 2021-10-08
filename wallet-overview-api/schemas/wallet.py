from datetime import datetime, date
from pydantic import BaseModel
from typing import Optional

class Wallet(BaseModel):
    user_id: int
    platform_id: int
    name: str
    api_key: str
    api_secret: str
    passphrase: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
