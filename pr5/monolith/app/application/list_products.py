from app.domain.product import Product
from app.domain.repository import ProductRepository

from .cache import ProductsCache


class ListProducts:
    def __init__(self, repository: ProductRepository, cache: ProductsCache) -> None:
        self._repository = repository
        self._cache = cache

    def execute(self) -> list[Product]:
        cached = self._cache.get_products()
        if cached is not None:
            return cached
        products = self._repository.list()
        self._cache.set_products(products)
        return products
