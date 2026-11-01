import pytest

from app.domain.errors import ValidationError
from app.domain.product import Product


@pytest.mark.parametrize("name,price", [("", 10), ("   ", 10), ("Desk", -1), ("Desk", 0)])
def test_product_rejects_invalid_values(name: str, price: float) -> None:
    with pytest.raises(ValidationError):
        Product(id=None, name=name, price=price)


def test_product_normalizes_name_and_price() -> None:
    product = Product(id=1, name=" Desk ", price=10)
    assert product.name == "Desk"
    assert product.price == 10.0
