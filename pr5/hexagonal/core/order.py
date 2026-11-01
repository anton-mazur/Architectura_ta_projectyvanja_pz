from dataclasses import dataclass

from .errors import OrderValidationError


@dataclass(frozen=True, slots=True)
class Order:
    id: str | None
    sku: str
    qty: int

    def __post_init__(self) -> None:
        sku = self.sku.strip() if isinstance(self.sku, str) else ""
        if not sku:
            raise OrderValidationError("sku must not be empty")
        if isinstance(self.qty, bool) or not isinstance(self.qty, int) or self.qty <= 0:
            raise OrderValidationError("qty must be a positive integer")
        object.__setattr__(self, "sku", sku)
