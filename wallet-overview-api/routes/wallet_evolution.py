from fastapi import APIRouter
from config.db import conn
from models.index import wallets_evolutions
from schemas.index import Wallet_evolution
from datetime import datetime

wallet_evolution = APIRouter()

@wallet_evolution.get("/wallet_evolution/")
async def read_data():
    return conn.execute(wallets_evolutions.select()).fetchall()
    
@wallet_evolution.get("/wallet_evolution/user_platform_id/{user_id}/{platform_id}")
async def read_data_user_platform_id(user_id, platform_id):
    return conn.execute(wallets_evolutions.select().where(wallets_evolutions.c.user_id == user_id and wallets_evolutions.c.platform_id == platform_id)).fetchall()

@wallet_evolution.get("/wallet_evolution/{id}")
async def read_data_id(id: int):
    return conn.execute(wallets_evolutions.select().where(wallets_evolutions.c.id == id)).fetchall()

@wallet_evolution.post("/wallet_evolution/")
async def write_data(wallet_evolution: Wallet_evolution):
    conn.execute(wallets_evolutions.insert().values(
        user_id = wallet_evolution.user_id,
        platform_id = wallet_evolution.platform_id,
        date = wallet_evolution.date,
        timestamp = wallet_evolution.timestamp,
        wallet_value_BTC = wallet_evolution.wallet_value_BTC,
        wallet_value_USDT = wallet_evolution.wallet_value_USDT
    ))
    return conn.execute(wallets_evolutions.select()).fetchall()

@wallet_evolution.put("/wallet_evolution/{id}")
async def update_data(id : int, wallet_evolution: Wallet_evolution):
    conn.execute(wallets_evolutions.update(
        user_id = wallet_evolution.user_id,
        platform_id = wallet_evolution.platform_id,
        date = wallet_evolution.date,
        timestamp = wallet_evolution.timestamp,
        wallet_value_BTC = wallet_evolution.wallet_value_BTC,
        wallet_value_USDT = wallet_evolution.wallet_value_USDT
    ).where(wallets_evolutions.c.id == id))
    return conn.execute(wallets_evolutions.select()).fetchall()

@wallet_evolution.delete("/wallet_evolution/{id}")
async def delete_data(id: int):
    conn.execute(wallets_evolutions.delete().where(wallets_evolutions.c.id == id))
    return conn.execute(wallets_evolutions.select()).fetchall()

@wallet_evolution.delete("/wallet_evolution/user_platform_id/{user_id}/{platform_id}")
async def delete_data_user_platform_id(user_id, platform_id):
    conn.execute(wallets_evolutions.delete().where(wallets_evolutions.c.user_id == user_id and wallets_evolutions.c.platform_id == platform_id))
    return conn.execute(wallets_evolutions.select()).fetchall()
