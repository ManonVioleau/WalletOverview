from fastapi import APIRouter
from config.db import conn
from models.index import trades_closed
from schemas.index import Trade_closed
from datetime import datetime

trade_closed = APIRouter()

@trade_closed.get("/trade_closed/")
async def read_data():
    return conn.execute(trades_closed.select()).fetchall()
    
@trade_closed.get("/trade_closed/user_platform_id/{user_id}/{platform_id}")
async def read_data_user_platform_id(user_id, platform_id):
    return conn.execute(trades_closed.select().where(trades_closed.c.user_id == user_id and trades_closed.c.platform_id == platform_id)).fetchall()

@trade_closed.get("/trade_closed/{id}")
async def read_data_id(id: int):
    return conn.execute(trades_closed.select().where(trades_closed.c.id == id)).fetchall()

@trade_closed.post("/trade_closed/")
async def write_data(trade_closed: Trade_closed):
    conn.execute(trades_closed.insert().values(
        user_id= trade_closed.user_id,
        platform_id= trade_closed.platform_id,
        date = trade_closed.date,
        timestamp = trade_closed.timestamp,
        type = trade_closed.type,
        symbol = trade_closed.symbol,
        received_currency = trade_closed.received_currency,
        received_quantity = trade_closed.received_quantity,
        sent_currency = trade_closed.sent_currency,
        sent_quantity = trade_closed.sent_quantity,
        fee_currency = trade_closed.fee_currency,
        fee_quantity = trade_closed.fee_quantity,
        trade_value = trade_closed.trade_value,
        fee_value = trade_closed.fee_value,
        orderId = trade_closed.orderId
    ))
    return conn.execute(trades_closed.select()).fetchall()

@trade_closed.put("/trade_closed/{id}")
async def update_data(id : int, trade_closed: Trade_closed):
    conn.execute(trades_closed.update(
        user_id= trade_closed.user_id,
        platform_id= trade_closed.platform_id,
        date = trade_closed.date,
        timestamp = trade_closed.timestamp,
        type = trade_closed.type,
        symbol = trade_closed.symbol,
        received_currency = trade_closed.received_currency,
        received_quantity = trade_closed.received_quantity,
        sent_currency = trade_closed.sent_currency,
        sent_quantity = trade_closed.sent_quantity,
        fee_currency = trade_closed.fee_currency,
        fee_quantity = trade_closed.fee_quantity,
        trade_value = trade_closed.trade_value,
        fee_value = trade_closed.fee_value,
        orderId = trade_closed.orderId
    ).where(trades_closed.c.id == id))
    return conn.execute(trades_closed.select()).fetchall()

@trade_closed.delete("/trade_closed/{id}")
async def delete_data(id: int):
    conn.execute(trades_closed.delete().where(trades_closed.c.id == id))
    return conn.execute(trades_closed.select()).fetchall()

@trade_closed.delete("/trade_closed/user_platform_id/{user_id}/{platform_id}")
async def delete_data_user_platform_id(user_id, platform_id):
    conn.execute(trades_closed.delete().where(trades_closed.c.user_id == user_id and trades_closed.c.platform_id == platform_id))
    return conn.execute(trades_closed.select()).fetchall()
