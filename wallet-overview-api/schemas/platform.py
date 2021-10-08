from datetime import date
from pydantic import BaseModel
from typing import Optional

class Platform(BaseModel):
    platform_name: str
    object_name: str