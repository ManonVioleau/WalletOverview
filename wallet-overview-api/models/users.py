from sqlalchemy import Table, Column, Integer, String, UniqueConstraint
from config.db import meta

users = Table(
    'users', meta, 
    Column('id', Integer, primary_key=True),
    Column('name', String(255), unique=True),
    Column('email', String(255), unique=True),
    Column('password', String(255)),
    UniqueConstraint('name', 'email')
)
