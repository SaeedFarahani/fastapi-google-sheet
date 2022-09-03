from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# from api.core import config
import os
from ttutils.TTConfigHandler import confighandler

DB_CON_STRING = confighandler.get_config("DB_CON_STRING_ASSIGNMENT", "")
CUS_DATA = confighandler.get_config("CUS_DATA", "/srv/cus_data")
database_dir = os.path.join(CUS_DATA, 'database/')

print(f'DB_CON_STRING: {DB_CON_STRING}')
print(f'CUS_DATA: {CUS_DATA}')
print(f'database_dir: {database_dir}')

if "sqlite" in DB_CON_STRING:
    #SQLALCHEMY_DATABASE_URL = "sqlite:///" + os.path.join(config.database_dir, "sql_app.db")
    print("sqlite")
    engine = create_engine(DB_CON_STRING, connect_args={
                           "check_same_thread": False})
elif "mysql" in DB_CON_STRING:
    engine = create_engine(DB_CON_STRING)

elif "oracle" in DB_CON_STRING:
    engine = create_engine(DB_CON_STRING)

# This called before base inialization
if not os.path.exists(database_dir):
    os.makedirs(database_dir)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
