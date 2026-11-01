import os
from datetime import datetime, timezone
from uuid import uuid4

from fastapi import FastAPI, status
from kafka import KafkaProducer
from pydantic import BaseModel, Field

BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")
app = FastAPI(title="Event orders")

class CreateOrder(BaseModel):
    userId: int = Field(gt=0)
    itemId: int = Field(gt=0)
    qty: int = Field(gt=0)

def producer() -> KafkaProducer:
    return KafkaProducer(bootstrap_servers=BROKER, value_serializer=lambda value: __import__("json").dumps(value).encode())

@app.get("/health")
def health(): return {"status": "ok"}

@app.post("/orders", status_code=status.HTTP_201_CREATED)
def create_order(payload: CreateOrder):
    event = {"type": "OrderCreated", "eventId": str(uuid4()), "orderId": str(uuid4()), **payload.model_dump(), "ts": datetime.now(timezone.utc).isoformat()}
    client = producer()
    client.send("orders.events", event).get(timeout=10)
    client.flush(); client.close()
    return {"id": event["orderId"]}
