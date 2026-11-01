import json
import os

from kafka import KafkaConsumer, KafkaProducer

from processor import BillingProcessor

broker = os.getenv("KAFKA_BROKER", "kafka:9092")
processor = BillingProcessor()
consumer = KafkaConsumer("orders.events", bootstrap_servers=broker, group_id="billing", auto_offset_reset="earliest", value_deserializer=lambda data: json.loads(data.decode()))
producer = KafkaProducer(bootstrap_servers=broker, value_serializer=lambda value: json.dumps(value).encode())

for message in consumer:
    payment = processor.process(message.value)
    if payment:
        producer.send("orders.events", payment).get(timeout=10)
        print(f"PaymentCaptured order={payment['orderId']}", flush=True)
