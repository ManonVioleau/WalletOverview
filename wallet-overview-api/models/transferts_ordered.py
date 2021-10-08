from sqlalchemy import Table, Column, Integer, String, Date, Float, DateTime, ForeignKey
from config.db import meta
from datetime import datetime

transferts_ordered = Table(
    'transferts_ordered', meta, 
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey("users.id")),
    Column('platform_id', Integer, ForeignKey("platforms.id")),
    Column('date', Date),
    Column('timestamp', String(255)),
    Column('value', Float),
)