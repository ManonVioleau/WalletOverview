from fastapi import APIRouter
from config.db import conn
from models.index import balances
from schemas.index import Balance
from datetime import datetime

balance = APIRouter()

@balance.get("/balance/")
async def read_data():
    return conn.execute(balances.select()).fetchall()
    
@balance.get("/balance/user_platform_id/{user_id}/{platform_id}")
async def read_data_user_platform_id(user_id, platform_id):
    return conn.execute(balances.select().where(balances.c.user_id == user_id and balances.c.platform_id == platform_id)).fetchall()

@balance.get("/balance/{id}")
async def read_data_id(id: int):
    return conn.execute(balances.select().where(balances.c.id == id)).fetchall()

@balance.post("/balance/")
async def write_data(balance: Balance):
    conn.execute(balances.insert().values(
        user_id = balance.user_id,
        platform_id = balance.platform_id,
        coin = balance.coin,
        quantity_free = balance.quantity_free,
        quantity_locked = balance.quantity_locked,
        quantity_total = balance.quantity_total,
        value = balance.value,
        created_at = datetime.now(),
        updated_at = datetime.now()
    ))
    return conn.execute(balances.select()).fetchall()

@balance.put("/balance/{id}")
async def update_data(id : int, balance: Balance):
    conn.execute(balances.update(
        user_id = balance.user_id,
        platform_id = balance.platform_id,
        coin = balance.coin,
        quantity_free = balance.quantity_free,
        quantity_locked = balance.quantity_locked,
        quantity_total = balance.quantity_total,
        value = balance.value,
        updated_at = datetime.now()
    ).where(balances.c.id == id))
    return conn.execute(balances.select()).fetchall()

@balance.delete("/balance/{id}")
async def delete_data(id: int):
    conn.execute(balances.delete().where(balances.c.id == id))
    return conn.execute(balances.select()).fetchall()

@balance.delete("/balance/user_platform_id/{user_id}/{platform_id}")
async def delete_data_user_platform_id(user_id, platform_id):
    conn.execute(balances.delete().where(balances.c.user_id == user_id and balances.c.platform_id == platform_id))
    return conn.execute(balances.select()).fetchall()
