from fastapi import APIRouter
from config.db import conn
from models.index import wallets
from schemas.index import Wallet
from routes.platform import read_data_id as read_platform_name
from datetime import datetime

from binance.client import Client
from binance.exceptions import BinanceAPIException

wallet = APIRouter()

@wallet.get("/wallet/")
async def read_data():
    return conn.execute(wallets.select()).fetchall()

@wallet.get("/wallet/{id}")
async def read_data_id(id: int):
    return conn.execute(wallets.select().where(wallets.c.id == id)).fetchall()

@wallet.get("/wallet/user_id/{user_id}")
async def read_data_user_platform_id(user_id):
    return conn.execute(wallets.select().where(wallets.c.user_id == user_id)).fetchall()

@wallet.post("/wallet/")
async def write_data(wallet: Wallet):
    check_wallet = conn.execute(wallets.select().where((wallets.c.name == wallet.name and wallets.c.user_id == wallet.user_id and wallets.c.platform_id == wallet.platform_id) or (wallets.c.api_key == wallet.api_key and wallets.c.user_id == wallet.user_id and wallets.c.platform_id == wallet.platform_id))).fetchone()
    if check_wallet == None:
        platform = await read_platform_name(wallet.platform_id)
        if platform[1] == 'Binance':
            try:
                client = Client(wallet.api_key, wallet.api_secret)
                client.get_account()
            except BinanceAPIException as e:
                return {"message": str(e), "data": None, "success": False}
            conn.execute(wallets.insert().values(
                user_id = wallet.user_id,
                platform_id = wallet.platform_id,
                name = wallet.name,
                api_key = wallet.api_key,
                api_secret = wallet.api_secret,
                passphrase = wallet.passphrase,
                created_at = datetime.now(),
                updated_at = datetime.now()
            ))
            check_wallet = conn.execute(wallets.select().where(wallets.c.name == wallet.name)).fetchone()
            return {"message": "Wallet Successfully added", "data": check_wallet, "success": True}
    else:
        return {"message": "Wallet already registred", "data": check_wallet, "success": False}


@wallet.put("/wallet/{id}")
async def update_data(id : int, wallet: Wallet):
    conn.execute(wallets.update(
        user_id = wallet.user_id,
        platform_id = wallet.platform_id,
        name = wallet.name,
        api_key = wallet.api_key,
        api_secret = wallet.api_secret,
        passphrase = wallet.passphrase,
        updated_at = datetime.now
    ).where(wallets.c.id == id))
    return conn.execute(wallets.select()).fetchall()

@wallet.delete("/wallet/{id}")
async def delete_data(id: int):
    conn.execute(wallets.delete().where(wallets.c.id == id))
    return conn.execute(wallets.select()).fetchall()
