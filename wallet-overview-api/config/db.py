from sqlalchemy import create_engine, MetaData
from config.id_connect import login, password, db_name

meta = MetaData()

engine = create_engine(f"mysql+pymysql://{login}:{password}@localhost:3306/{db_name}")

conn = engine.connect()