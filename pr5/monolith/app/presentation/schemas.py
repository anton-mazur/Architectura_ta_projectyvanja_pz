from pydantic import BaseModel, Field


class CreateProductRequest(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    price: float = Field(gt=0)


class ProductResponse(BaseModel):
    id: int
    name: str
    price: float


class CreateProductResponse(BaseModel):
    id: int
