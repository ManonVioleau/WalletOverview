from sqlalchemy import Table, Column, Integer, String, Date, Float, DateTime, ForeignKey
from config.db import meta
from datetime import datetime

trades_closed = Table(
    'trades_closed', meta, 
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey("users.id")),
    Column('platform_id', Integer, ForeignKey("platforms.id")),
    Column('date', Date),
    Column('timestamp', String(255)),
    Column('type', String(255)),
    Column('symbol', String(255)),
    Column('received_currency', String(255)),
    Column('received_quantity', Float),
    Column('sent_currency', String(255)),
    Column('sent_quantity', Float),
    Column('fee_currency', String(255)),
    Column('fee_quantity', Float),
    Column('trade_value', Float),
    Column('fee_value', Float),
    Column('orderId', String(255)),
)