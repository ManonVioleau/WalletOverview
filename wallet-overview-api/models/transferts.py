from sqlalchemy import Table, Column, Integer, String, Date, Float, DateTime, ForeignKey
from config.db import meta
from datetime import datetime

transferts = Table(
    'transferts', meta, 
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey("users.id")),
    Column('platform_id', Integer, ForeignKey("platforms.id")),
    Column('date', Date),
    Column('timestamp', String(255)),
    Column('type', String(255)),
    Column('coin', String(255)),
    Column('quantity', Float),
    Column('fees', Float, nullable=True),
    Column('transfert_value', Float),
    Column('fee_value', Float, nullable=True),
    Column('network', String(255)),
    Column('address', String(255)),
    Column('status', String(255)),
    Column('dep_with_value', Float),
)