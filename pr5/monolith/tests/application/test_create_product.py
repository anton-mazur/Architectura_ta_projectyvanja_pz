import pytest

from app.application.create_product import CreateProduct
from app.application.dto import CreateProductDTO
from app.domain.errors import ValidationError
from app.domain.product import Product


class FakeRepository:
    def __init__(self) -> None:
        self.created: list[Product] = []

    def create(self, product: Product) -> Product:
        saved = Product(id=len(self.created) + 1, name=product.name, price=product.price)
        self.created.append(saved)
        return saved

    def list(self) -> list[Product]:
        return self.created


class FakeCache:
    def __init__(self) -> None:
        self.invalidated = False

    def get_products(self): return None
    def set_products(self, products): pass
    def invalidate_products(self): self.invalidated = True


def test_create_product_persists_through_repository() -> None:
    repository, cache = FakeRepository(), FakeCache()
    created = CreateProduct(repository, cache).execute(CreateProductDTO("Desk", 199.9))
    assert created.id == 1
    assert repository.created == [created]
    assert cache.invalidated


def test_create_product_rejects_invalid_input_before_repository() -> None:
    with pytest.raises(ValidationError):
        CreateProduct(FakeRepository(), FakeCache()).execute(CreateProductDTO("", 10))
