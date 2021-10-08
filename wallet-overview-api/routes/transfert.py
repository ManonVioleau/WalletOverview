from fastapi import APIRouter
from config.db import conn
from models.index import transferts
from schemas.index import Transfert
from datetime import datetime

transfert = APIRouter()

@transfert.get("/transfert/")
async def read_data():
    return conn.execute(transferts.select()).fetchall()
    
@transfert.get("/transfert/user_platform_id/{user_id}/{platform_id}")
async def read_data_user_platform_id(user_id, platform_id):
    return conn.execute(transferts.select().where(transferts.c.user_id == user_id and transferts.c.platform_id == platform_id)).fetchall()

@transfert.get("/transfert/{id}")
async def read_data_id(id: int):
    return conn.execute(transferts.select().where(transferts.c.id == id)).fetchall()

@transfert.post("/transfert/")
async def write_data(transfert: Transfert):
    conn.execute(transferts.insert().values(
        user_id= transfert.user_id,
        platform_id= transfert.platform_id,
        date = transfert.date,
        timestamp = transfert.timestamp,
        type = transfert.type,
        coin = transfert.coin,
        quantity = transfert.quantity,
        fees = transfert.fees,
        transfert_value = transfert.transfert_value,
        fee_value = transfert.fee_value,
        network = transfert.network,
        address = transfert.address,
        status = transfert.status,
        dep_with_value = transfert.dep_with_value
    ))
    return conn.execute(transferts.select()).fetchall()

@transfert.put("/transfert/{id}")
async def update_data(id : int, transfert: Transfert):
    conn.execute(transferts.update(
        user_id= transfert.user_id,
        platform_id= transfert.platform_id,
        date = transfert.date,
        timestamp = transfert.timestamp,
        type = transfert.type,
        coin = transfert.coin,
        quantity = transfert.quantity,
        fees = transfert.fees,
        transfert_value = transfert.transfert_value,
        fee_value = transfert.fee_value,
        network = transfert.network,
        address = transfert.address,
        status = transfert.status,
        dep_with_value = transfert.dep_with_value
    ).where(transferts.c.id == id))
    return conn.execute(transferts.select()).fetchall()

@transfert.delete("/transfert/{id}")
async def delete_data(id: int):
    conn.execute(transferts.delete().where(transferts.c.id == id))
    return conn.execute(transferts.select()).fetchall()

@transfert.delete("/transfert/user_platform_id/{user_id}/{platform_id}")
async def delete_data_user_platform_id(user_id, platform_id):
    conn.execute(transferts.delete().where(transferts.c.user_id == user_id and transferts.c.platform_id == platform_id))
    return conn.execute(transferts.select()).fetchall()
