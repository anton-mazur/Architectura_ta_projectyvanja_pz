import pytest

from core.errors import OrderValidationError
from core.order import Order
from core.usecases import CreateOrder, GetOrder


class MemoryRepository:
    def __init__(self): self.orders = {}
    def create(self, order):
        order_id = "o-1"; self.orders[order_id] = Order(order_id, order.sku, order.qty); return order_id
    def get_by_id(self, order_id): return self.orders.get(order_id)


def test_order_validates_qty():
    with pytest.raises(OrderValidationError): Order(None, "SKU", 0)


def test_use_cases_delegate_to_port():
    repository = MemoryRepository()
    order_id = CreateOrder(repository).execute("ABC", 2)
    assert GetOrder(repository).execute(order_id) == Order("o-1", "ABC", 2)
