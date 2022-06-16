# app/config.py

from functools import lru_cache

# pydantic is a library that uses type annotation to validate data and manage 
from pydantic import BaseSettings # pylint: disable=import-error

"""
a subclass of BaseSettings. The BaseSettings class comes in handy to define environment variables in your application. You only have to define the variables that you want to use, and pydantic takes care of the rest. 
In other words, pydantic will automatically assume those default values if it doesn’t find the corresponding environment variables.
"""
# defining default variables 
class Settings(BaseSettings): 
    # Name of your current environment
    env_name: str = "Local"
    # Domain of your app
    base_url: str = "http://localhost:8000"
    # Address of your database
    db_url: str = "sqlite:///./shortener.db"
    # TODO:
    # root of your project directory. 
    class Config:
        env_file = ".env"

#  Least Recently Used (LRU) 
@lru_cache
# the option of caching your settings. 
def get_settings() -> Settings: 
    
    settings = Settings()

    print(f"Loading settings for: {settings.env_name}")
    # default return of get_settings
    return settings