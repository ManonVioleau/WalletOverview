from sqlalchemy import Table, Column, Integer, String, Date, Float, DateTime, ForeignKey
from config.db import meta
from datetime import datetime

trades_open = Table(
    'trades_open', meta, 
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey("users.id")),
    Column('platform_id', Integer, ForeignKey("platforms.id")),
    Column('date', Date),
    Column('timestamp', String(255)),
    Column('type', String(255)),
    Column('symbol', String(255)),
    Column('quantity', Float),
    Column('price', Float),
)