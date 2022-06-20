# app/database.py 

from enum import auto
from sqlite3 import connect
from sqlalchemy import create_engine
#  returns a class that connects the database engine to the SQLAlchemy functionality of the models. 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import get_settings


#  SQLite allows more than one request at a time to communicate with the database.
engine = create_engine(
    get_settings().db_url, connect_args={
        "check_same_thread": False
    }
)

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)
# Base will be the class that the database model inherits from in your models.py file.
Base = declarative_base()


