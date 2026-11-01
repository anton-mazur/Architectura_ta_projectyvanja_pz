from fastapi.testclient import TestClient

from app.domain.product import Product
from app.main import create_app


class MemoryRepository:
    def __init__(self) -> None:
        self.items: list[Product] = []

    def create(self, product: Product) -> Product:
        saved = Product(id=len(self.items) + 1, name=product.name, price=product.price)
        self.items.append(saved)
        return saved

    def list(self) -> list[Product]:
        return list(self.items)


class MemoryCache:
    def __init__(self) -> None: self.value = None
    def get_products(self): return self.value
    def set_products(self, products): self.value = list(products)
    def invalidate_products(self): self.value = None


def test_products_api_smoke() -> None:
    client = TestClient(create_app(MemoryRepository(), MemoryCache()))
    assert client.get("/health").json() == {"status": "ok"}
    created = client.post("/products", json={"name": "Desk", "price": 199.9})
    assert created.status_code == 201
    assert created.json() == {"id": 1}
    assert client.get("/products").json() == [{"id": 1, "name": "Desk", "price": 199.9}]
