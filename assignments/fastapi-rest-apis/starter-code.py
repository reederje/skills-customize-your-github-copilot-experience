"""
FastAPI starter app for the assignment.

Run:
  pip install -r requirements.txt
  uvicorn starter-code:app --reload

This file provides a minimal example with in-memory storage.
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="FastAPI Starter")


class Item(BaseModel):
    id: int
    name: str
    price: float


# Simple in-memory "database"
db = {}


@app.get("/")
def read_root():
    return {"message": "FastAPI starter - API is running"}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    item = db.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/items", status_code=201)
def create_item(item: Item):
    if item.id in db:
        raise HTTPException(status_code=400, detail="ID already exists")
    db[item.id] = item.dict()
    return db[item.id]
