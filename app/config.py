# app/config.py


from pydantic import BaseSettings # pylint: disable=import-error

"""
a subclass of BaseSettings. The BaseSettings class comes in handy to define environment variables in your application. You only have to define the variables that you want to use, and pydantic takes care of the rest. 
In other words, pydantic will automatically assume those default values if it doesn’t find the corresponding environment variables.
"""
class Settings(BaseSettings): 

    env_name: str = "Local"

    base_url: str = "http://localhost:8000"

    db_url: str = "sqlite:///./shortener.db"


def get_settings() -> Settings: 

    settings = Settings()

    print(f"Loading settings for: {settings.env_name}")

    return settings