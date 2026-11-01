from typing import Any

from fastapi import FastAPI, HTTPException, Request, status
from pydantic import BaseModel, Field

from core.errors import OrderValidationError


class CreateOrderRequest(BaseModel):
    sku: str = Field(min_length=1)
    qty: int = Field(gt=0)


def create_http_app(create_order: Any, get_order: Any) -> FastAPI:
    app = FastAPI(title="Hexagonal Orders")
    app.state.create_order = create_order
    app.state.get_order = get_order

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok"}

    @app.post("/orders", status_code=status.HTTP_201_CREATED)
    def create(payload: CreateOrderRequest, request: Request) -> dict[str, str]:
        try:
            order_id = request.app.state.create_order.execute(payload.sku, payload.qty)
        except OrderValidationError as exc:
            raise HTTPException(422, str(exc)) from exc
        return {"id": order_id}

    @app.get("/orders/{order_id}")
    def get(order_id: str, request: Request) -> dict[str, Any]:
        order = request.app.state.get_order.execute(order_id)
        if order is None:
            raise HTTPException(404, "order not found")
        return {"id": order.id, "sku": order.sku, "qty": order.qty}

    return app
