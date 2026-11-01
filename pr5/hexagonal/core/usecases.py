from .order import Order
from .ports import OrderRepository


class CreateOrder:
    def __init__(self, repository: OrderRepository) -> None:
        self._repository = repository

    def execute(self, sku: str, qty: int) -> str:
        return self._repository.create(Order(id=None, sku=sku, qty=qty))


class GetOrder:
    def __init__(self, repository: OrderRepository) -> None:
        self._repository = repository

    def execute(self, order_id: str) -> Order | None:
        return self._repository.get_by_id(order_id)
