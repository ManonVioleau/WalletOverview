from sqlalchemy import Table, Column, Integer, String, Date, Float, ForeignKey
from config.db import meta

platforms = Table(
    'platforms', meta, 
    Column('id', Integer, primary_key=True),
    Column('platform_name', String(255)),
    Column('object_name', String(255)),
)