import json
import os
from datetime import datetime, timezone
from uuid import uuid4

from kafka import KafkaConsumer, KafkaProducer

broker = os.getenv("KAFKA_BROKER", "kafka:9092")
consumer = KafkaConsumer("orders.events", bootstrap_servers=broker, group_id="notifications", auto_offset_reset="earliest", value_deserializer=lambda data: json.loads(data.decode()))
producer = KafkaProducer(bootstrap_servers=broker, value_serializer=lambda value: json.dumps(value).encode())

for message in consumer:
    payment = message.value
    if payment.get("type") != "PaymentCaptured":
        continue
    email = {"type": "EmailSent", "eventId": str(uuid4()), "orderId": payment["orderId"], "to": "user@example.com", "ts": datetime.now(timezone.utc).isoformat()}
    print(f"EmailSent order={email['orderId']} to={email['to']}", flush=True)
    producer.send("orders.events", email).get(timeout=10)
