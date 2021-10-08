from pydantic import BaseModel

class User_Platform(BaseModel):
    user_id: int
    platform_id: int