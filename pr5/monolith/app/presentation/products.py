from fastapi import APIRouter, HTTPException, Request, status

from app.application.dto import CreateProductDTO
from app.domain.errors import ValidationError

from .schemas import CreateProductRequest, CreateProductResponse, ProductResponse

router = APIRouter(prefix="/products", tags=["products"])


@router.get("", response_model=list[ProductResponse])
def list_products(request: Request) -> list[ProductResponse]:
    products = request.app.state.list_products.execute()
    return [ProductResponse(id=p.id, name=p.name, price=p.price) for p in products]


@router.post("", response_model=CreateProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(payload: CreateProductRequest, request: Request) -> CreateProductResponse:
    try:
        product = request.app.state.create_product.execute(
            CreateProductDTO(name=payload.name, price=payload.price)
        )
    except ValidationError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    return CreateProductResponse(id=product.id)
