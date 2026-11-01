from typing import Protocol

from app.domain.product import Product


class ProductsCache(Protocol):
    def get_products(self) -> list[Product] | None: ...

    def set_products(self, products: list[Product]) -> None: ...

    def invalidate_products(self) -> None: ...
