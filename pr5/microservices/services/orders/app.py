from itertools import count

from fastapi import FastAPI, status
from pydantic import BaseModel, Field

app = FastAPI(title="Orders service")
ids = count(1)
orders = []

class CreateOrder(BaseModel):
    userId: int = Field(gt=0)
    itemId: int = Field(gt=0)
    qty: int = Field(gt=0)

@app.get("/health")
def health(): return {"status": "ok"}

@app.post("/orders", status_code=status.HTTP_201_CREATED)
def create_order(payload: CreateOrder):
    order = {"id": next(ids), **payload.model_dump()}
    orders.append(order)
    return {"id": order["id"]}
