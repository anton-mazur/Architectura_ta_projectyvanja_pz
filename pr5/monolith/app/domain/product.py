from dataclasses import dataclass
from math import isfinite

from .errors import ValidationError


@dataclass(frozen=True, slots=True)
class Product:
    id: int | None
    name: str
    price: float

    def __post_init__(self) -> None:
        if self.id is not None and (isinstance(self.id, bool) or not isinstance(self.id, int) or self.id <= 0):
            raise ValidationError("id must be a positive integer")
        name = self.name.strip() if isinstance(self.name, str) else ""
        if not 1 <= len(name) <= 100:
            raise ValidationError("name must contain from 1 to 100 characters")
        if (
            isinstance(self.price, bool)
            or not isinstance(self.price, (int, float))
            or not isfinite(self.price)
            or self.price <= 0
        ):
            raise ValidationError("price must be greater than zero")
        object.__setattr__(self, "name", name)
        object.__setattr__(self, "price", float(self.price))
