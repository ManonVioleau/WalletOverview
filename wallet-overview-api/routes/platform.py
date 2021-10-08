from fastapi import APIRouter
from config.db import conn
from models.index import platforms
from schemas.index import Platform

platform = APIRouter()

@platform.get("/platform/")
async def read_data():
    return conn.execute(platforms.select()).fetchall()

@platform.get("/platform/{id}")
async def read_data_id(id: int):
    return conn.execute(platforms.select().where(platforms.c.id == id)).fetchone()

@platform.get("/platform_by_name/{name}")
async def read_data_name(name: str):
    platform = conn.execute(platforms.select().where(platforms.c.platform_name == name)).fetchone()
    return {"message": "Platform found", "data": platform}

@platform.post("/platform/")
async def write_data(platform: Platform):
    conn.execute(platforms.insert().values(
        platform_name = platform.platform_name,
        object_name = platform.object_name,
    ))
    return conn.execute(platforms.select()).fetchall()

@platform.put("/platform/{id}")
async def update_data(id : int, platform: Platform):
    conn.execute(platforms.update(
        platform_name = platform.platform_name,
        object_name = platform.object_name,
    ).where(platforms.c.id == id))
    return conn.execute(platforms.select()).fetchall()

@platform.delete("/platform/{id}")
async def delete_data(id: int):
    conn.execute(platforms.delete().where(platforms.c.id == id))
    return conn.execute(platforms.select()).fetchall()
