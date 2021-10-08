from sqlalchemy import Table, Column, Integer, String, Date, Float, DateTime, ForeignKey
from config.db import meta
from datetime import datetime

balances = Table(
    'balances', meta, 
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey("users.id")),
    Column('platform_id', Integer, ForeignKey("platforms.id")),
    Column('coin', String(255)),
    Column('quantity_free', Float),
    Column('quantity_locked', Float),
    Column('quantity_total', Float),
    Column('value', Float),
    Column('created_at', DateTime, default=datetime.now),
    Column('updated_at', DateTime, default=datetime.now)
)