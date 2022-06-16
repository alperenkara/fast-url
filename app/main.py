# app/main.py 

import re
import validators
from fastapi import FastAPI,HTTPException
from . import schemas
# main point of interaction to create the API. 
app = FastAPI()

def raise_bad_request(message):
    raise HTTPException(status_code=400, detail=message)

# path operation decorator
@app.get("/")
# FastAPI listens to the root path and delegates all incoming GET requests to your read_root() function.
def read_root():
    return "First-1 version of the URL shortener"


@app.post("/url")
def create_url(url: schemas.URLBase):
    if not validators.url(url.target_url):
        raise_bad_request(message="URL is not valid")
    return f"TODO:Create DB entry for : {url.target_url}"