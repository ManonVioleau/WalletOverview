from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemas.index import User
import bcrypt

user = APIRouter()

@user.get("/users/")
async def read_data():
    return conn.execute(users.select()).fetchall()

@user.get("/users/{id}")
async def read_data_id(id: int):
    return conn.execute(users.select().where(users.c.id == id)).fetchall()

@user.post("/users/register/")
async def write_data(user: User):
    check_user_name = conn.execute(users.select().where(users.c.name == user.name)).fetchone()
    check_user_email = conn.execute(users.select().where(users.c.email == user.email)).fetchone()
    if check_user_name == None and check_user_email == None:
        password = f"{user.password}".encode("utf-8")
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        conn.execute(users.insert().values(
            name=user.name,
            email=user.email,
            password=hashed
        ))
        user = conn.execute(users.select().where(users.c.name == user.name)).fetchone()
        return {'message': 'User successfully register', 'data': user, 'success': True}
    else:
        return {'message': 'Username or Email already exists', 'data': None, 'success': False}

@user.post("/users/login/")
async def write_data(user: User):
    check_user = conn.execute(users.select().where(users.c.name == user.name)).fetchone()
    if check_user == None:
        return {'message': 'Seems like there is a problem in your Username or password', 'data': None, 'success': False}
    else:
        password_gave = f"{user.password}".encode("utf-8")
        password_bdd = f"{check_user.password}".encode("utf-8")
        if bcrypt.checkpw(password_gave, password_bdd):
            return {'message': 'User successfully logged', 'data': check_user, 'success': True}
        else:
            return {'message': 'Seems like there is a problem in your Username or Password', 'data': None, 'success': False}

@user.put("/users/{id}")
async def update_data(id : int, user: User):
    password = bcrypt(user.password)
    conn.execute(users.update(
        name=user.name,
        email=user.email,
        password=password
    ).where(users.c.id == id))
    return conn.execute(users.select()).fetchall()

@user.delete("/users/{id}")
async def delete_data(id: int):
    conn.execute(users.delete().where(users.c.id == id))
    return conn.execute(users.select()).fetchall()
