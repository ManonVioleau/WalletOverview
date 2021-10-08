from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class Synchronisation(BaseModel):
    user_id: int
    platform_id: int
    new_user: bool
