from datetime import datetime, timezone
from uuid import uuid4


class BillingProcessor:
    """In-memory idempotency store; replace with a durable table in production."""
    def __init__(self) -> None:
        self.processed_event_ids: set[str] = set()

    def process(self, event: dict) -> dict | None:
        if event.get("type") != "OrderCreated" or event["eventId"] in self.processed_event_ids:
            return None
        self.processed_event_ids.add(event["eventId"])
        return {
            "type": "PaymentCaptured", "eventId": str(uuid4()), "orderId": event["orderId"],
            "amount": event["qty"] * 100, "ts": datetime.now(timezone.utc).isoformat(),
        }
