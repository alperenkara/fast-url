# app/main.py 
from io import DEFAULT_BUFFER_SIZE
import secrets
import re
from statistics import mode
# validator package check the URL string is whether valid or not. 
import validators
from fastapi import Depends, FastAPI,HTTPException, Request
# RedirectResponse returns an HTTP redirect that forwards the request of the client.
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from . import models, schemas
from .database import SessionLocal, engine
# main point of interaction to create the API. 
app = FastAPI()

# if the database that you defined in engine doesn’t exist yet, then it’ll be created with all modeled tables once you run your app the first time.
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    # You use the try … finally block to close the database connection in any case, even when an error occurs during the request
    try:
        yield db 
    finally: 
        db.close()
        
        
@app.post("/url")
# stating create_url endpoint 
# URL string as POST request body. 

def create_url(url: schemas.URLBase, db: Session = Depends(get_db)):
    # check URL, if it is not valid, pass it! 
    if not validators.url(url.target_url):
        raise_bad_request(message="URL is not valid")
    # return f"TODO:Create DB entry for : {url.target_url}"
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    key = "".join(secrets.choice(chars) for _ in range(5))
    secret_key = "".join(secrets.choice(chars) for _ in range(8))
    
    db_url = models.URL(

        target_url=url.target_url, key=key, secret_key=secret_key

    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    db_url.url = key
    db_url.admin_url = secret_key
    
    return db_url

def raise_bad_request(message):
    raise HTTPException(status_code=400, detail=message)

def raise_not_found(request):
    message = f"URL'{request.url}' does not exist"
    raise HTTPException(status_code=404,detail=message)

# you allow GET requests for the URL that you provide as an argument. 
@app.get("/{url_key}")
def forward_to_target_url(
    url_key: str,
    request: Request,
    db: Session = Depends(get_db)
):
    db_url = (
        db.query(models.URL)
        .filter(models.URL.key == url_key, models.URL.is_active)
        .first()
    )
    if db_url:
        return RedirectResponse(db_url.target_url)
    else:
        raise_not_found(request)
        
        
# path operation decorator
@app.get("/")
# FastAPI listens to the root path and delegates all incoming GET requests to your read_root() function.
def read_root():
    return "First-1 version of the URL shortener"
