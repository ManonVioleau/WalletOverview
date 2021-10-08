from sqlalchemy import Table, Column, Integer, String, Date, Float, DateTime, ForeignKey
from config.db import meta
from datetime import datetime

means_trades = Table(
    'means_trades', meta, 
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey("users.id")),
    Column('platform_id', Integer, ForeignKey("platforms.id")),
    Column('coin', String(255)),
    Column('mean_buy', Float),
    Column('mean_sell', Float),
    Column('buy_minus_sell', Float),
    Column('percent_gain_loss', Float)
)