from sqlalchemy import Table, Column, Integer, String, Date, Float, DateTime, ForeignKey
from config.db import meta
from datetime import datetime
import time

wallets = Table(
    'wallets', meta, 
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey("users.id")),
    Column('platform_id', Integer, ForeignKey("platforms.id")),
    Column('name', String(255)),
    Column('api_key', String(255)),
    Column('api_secret', String(255)),
    Column('passphrase', String(255), nullable=True),
    Column('created_at', DateTime, default=datetime.now()),
    Column('updated_at', DateTime, default=datetime.now())
)