from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CreateProductDTO:
    name: str
    price: float
