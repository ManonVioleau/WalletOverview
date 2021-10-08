from fastapi import APIRouter
from config.db import conn
from models.index import transferts_ordered
from schemas.index import Transfert_ordered
from datetime import datetime

transfert_ordered = APIRouter()

@transfert_ordered.get("/transfert_ordered/")
async def read_data():
    return conn.execute(transferts_ordered.select()).fetchall()
    
@transfert_ordered.get("/transfert_ordered/user_platform_id/{user_id}/{platform_id}")
async def read_data_user_platform_id(user_id, platform_id):
    return conn.execute(transferts_ordered.select().where(transferts_ordered.c.user_id == user_id and transferts_ordered.c.platform_id == platform_id)).fetchall()

@transfert_ordered.get("/transfert_ordered/{id}")
async def read_data_id(id: int):
    return conn.execute(transferts_ordered.select().where(transferts_ordered.c.id == id)).fetchall()

@transfert_ordered.post("/transfert_ordered/")
async def write_data(transfert_ordered: Transfert_ordered):
    conn.execute(transferts_ordered.insert().values(
        user_id= transfert_ordered.user_id,
        platform_id= transfert_ordered.platform_id,
        date = transfert_ordered.date,
        timestamp = transfert_ordered.timestamp,
        value = transfert_ordered.value
    ))
    return conn.execute(transferts_ordered.select()).fetchall()

@transfert_ordered.put("/transfert_ordered/{id}")
async def update_data(id : int, transfert_ordered: Transfert_ordered):
    conn.execute(transferts_ordered.update(
        user_id= transfert_ordered.user_id,
        platform_id= transfert_ordered.platform_id,
        date = transfert_ordered.date,
        timestamp = transfert_ordered.timestamp,
        value = transfert_ordered.value
    ).where(transferts_ordered.c.id == id))
    return conn.execute(transferts_ordered.select()).fetchall()

@transfert_ordered.delete("/transfert_ordered/{id}")
async def delete_data(id: int):
    conn.execute(transferts_ordered.delete().where(transferts_ordered.c.id == id))
    return conn.execute(transferts_ordered.select()).fetchall()

@transfert_ordered.delete("/transfert_ordered/user_platform_id/{user_id}/{platform_id}")
async def delete_data_user_platform_id(user_id, platform_id):
    conn.execute(transferts_ordered.delete().where(transferts_ordered.c.user_id == user_id and transferts_ordered.c.platform_id == platform_id))
    return conn.execute(transferts_ordered.select()).fetchall()
