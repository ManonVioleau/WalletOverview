from fastapi import APIRouter
from config.db import conn
from models.index import means_trades
from schemas.index import Mean_trade
from datetime import datetime

mean_trade = APIRouter()

@mean_trade.get("/mean_trade/")
async def read_data():
    return conn.execute(means_trades.select()).fetchall()
    
@mean_trade.get("/mean_trade/user_platform_id/{user_id}/{platform_id}")
async def read_data_user_platform_id(user_id, platform_id):
    return conn.execute(means_trades.select().where(means_trades.c.user_id == user_id and means_trades.c.platform_id == platform_id)).fetchall()

@mean_trade.get("/mean_trade/{id}")
async def read_data_id(id: int):
    return conn.execute(means_trades.select().where(means_trades.c.id == id)).fetchall()

@mean_trade.post("/mean_trade/")
async def write_data(mean_trade: Mean_trade):
    conn.execute(means_trades.insert().values(
        user_id= mean_trade.user_id,
        platform_id= mean_trade.platform_id,
        coin = mean_trade.coin,
        mean_buy = mean_trade.mean_buy,
        mean_sell = mean_trade.mean_sell,
        buy_minus_sell = mean_trade.buy_minus_sell,
        percent_gain_loss = mean_trade.percent_gain_loss
    ))
    return conn.execute(means_trades.select()).fetchall()

@mean_trade.put("/mean_trade/{id}")
async def update_data(id : int, mean_trade: Mean_trade):
    conn.execute(means_trades.update(
        user_id= mean_trade.user_id,
        platform_id= mean_trade.platform_id,
        coin = mean_trade.coin,
        mean_buy = mean_trade.mean_buy,
        mean_sell = mean_trade.mean_sell,
        buy_minus_sell = mean_trade.buy_minus_sell,
        percent_gain_loss = mean_trade.percent_gain_loss
    ).where(means_trades.c.id == id))
    return conn.execute(means_trades.select()).fetchall()

@mean_trade.delete("/mean_trade/{id}")
async def delete_data(id: int):
    conn.execute(means_trades.delete().where(means_trades.c.id == id))
    return conn.execute(means_trades.select()).fetchall()

@mean_trade.delete("/mean_trade/user_platform_id/{user_id}/{platform_id}")
async def delete_data_user_platform_id(user_id, platform_id):
    conn.execute(means_trades.delete().where(means_trades.c.user_id == user_id and means_trades.c.platform_id == platform_id))
    return conn.execute(means_trades.select()).fetchall()
