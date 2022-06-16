# app/main.py 


from fastapi import FastAPI

# main point of interaction to create the API. 
app = FastAPI()


# path operation decorator
@app.get("/")
# FastAPI listens to the root path and delegates all incoming GET requests to your read_root() function.
def read_root():
    return "First-1 version of the URL shortener"