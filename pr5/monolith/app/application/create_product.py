from app.domain.product import Product
from app.domain.repository import ProductRepository

from .cache import ProductsCache
from .dto import CreateProductDTO


class CreateProduct:
    def __init__(self, repository: ProductRepository, cache: ProductsCache) -> None:
        self._repository = repository
        self._cache = cache

    def execute(self, dto: CreateProductDTO) -> Product:
        product = Product(id=None, name=dto.name, price=dto.price)
        created = self._repository.create(product)
        self._cache.invalidate_products()
        return created
