from sqlalchemy import Table, Column, Integer, String, Date, Float, ForeignKey
from config.db import meta

wallets_evolutions = Table(
    'wallets_evolutions', meta, 
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey("users.id")),
    Column('platform_id', Integer, ForeignKey("platforms.id")),
    Column('date', Date),
    Column('timestamp', String(255)),
    Column('wallet_value_BTC', Float),
    Column('wallet_value_USDT', Float),
)
