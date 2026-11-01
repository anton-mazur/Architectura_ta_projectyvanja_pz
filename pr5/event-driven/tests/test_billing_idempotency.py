from services.billing.processor import BillingProcessor


def test_duplicate_order_created_produces_one_payment():
    processor = BillingProcessor()
    event = {"type": "OrderCreated", "eventId": "event-1", "orderId": "order-1", "qty": 2}
    assert processor.process(event)["orderId"] == "order-1"
    assert processor.process(event) is None
