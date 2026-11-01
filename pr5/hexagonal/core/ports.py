from typing import Protocol

from .order import Order


class OrderRepository(Protocol):
    def create(self, order: Order) -> str: ...

    def get_by_id(self, order_id: str) -> Order | None: ...
