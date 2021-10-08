from fastapi import APIRouter
from config.db import conn
from models.index import trades_open
from schemas.index import Trade_open
from datetime import datetime

trade_open = APIRouter()

@trade_open.get("/trade_open/")
async def read_data():
    return conn.execute(trades_open.select()).fetchall()
    
@trade_open.get("/trade_open/user_platform_id/{user_id}/{platform_id}")
async def read_data_user_platform_id(user_id, platform_id):
    return conn.execute(trades_open.select().where(trades_open.c.user_id == user_id and trades_open.c.platform_id == platform_id)).fetchall()

@trade_open.get("/trade_open/{id}")
async def read_data_id(id: int):
    return conn.execute(trades_open.select().where(trades_open.c.id == id)).fetchall()

@trade_open.post("/trade_open/")
async def write_data(trade_open: Trade_open):
    conn.execute(trades_open.insert().values(
        user_id= trade_open.user_id,
        platform_id= trade_open.platform_id,
        date = trade_open.date,
        timestamp = trade_open.timestamp,
        type = trade_open.type,
        symbol = trade_open.symbol,
        quantity = trade_open.quantity,
        price = trade_open.price
    ))
    return conn.execute(trades_open.select()).fetchall()

@trade_open.put("/trade_open/{id}")
async def update_data(id : int, trade_open: Trade_open):
    conn.execute(trades_open.update(
        user_id= trade_open.user_id,
        platform_id= trade_open.platform_id,
        date = trade_open.date,
        timestamp = trade_open.timestamp,
        type = trade_open.type,
        symbol = trade_open.symbol,
        quantity = trade_open.quantity,
        price = trade_open.price
    ).where(trades_open.c.id == id))
    return conn.execute(trades_open.select()).fetchall()

@trade_open.delete("/trade_open/{id}")
async def delete_data(id: int):
    conn.execute(trades_open.delete().where(trades_open.c.id == id))
    return conn.execute(trades_open.select()).fetchall()

@trade_open.delete("/trade_open/user_platform_id/{user_id}/{platform_id}")
async def delete_data_user_platform_id(user_id, platform_id):
    conn.execute(trades_open.delete().where(trades_open.c.user_id == user_id and trades_open.c.platform_id == platform_id))
    return conn.execute(trades_open.select()).fetchall()
