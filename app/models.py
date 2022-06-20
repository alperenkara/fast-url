# app/models.py

from enum import unique
from textwrap import indent
from sqlalchemy import Boolean, Column, Integer, String

from .database import Base


# Declaring how your data should be stored in the database.
# The URL model is a subclass of Base
class URL(Base):
    __tablename__ = "urls"
    # primary key
    id = Column(Integer, primary_key=True)

    key = Column(String, unique=True, index=True)

    secret_key = Column(String, unique=True, index=True)

    target_url = Column(String, index=True)
    # Instead of giving the user the power to delete a database entry directly, you’ll make the entry inactive instead. 
    is_active = Column(Boolean, default=True)

    clicks = Column(Integer, default=0)
    