from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()
@app.get("/")
def root():
    return {'start': '1970-01-01'}

@app.post("/method")
def method_post():
    return {"method": "POST"}

@app.get("/method")
def method_get():
    return {"method": "GET"}

@app.put("/method")
def method_put():
    return {"method": "PUT"}

@app.options("/method")
def method_options():
    return {"method": "OPTIONS"}

@app.delete("/method")
def method_delete():
    return {"method": "DELETE"}

@app.post("/method")
def method_post():
    return {"method": "POST"}