import os
from typing import Any

from fastapi import FastAPI

from app.application.create_product import CreateProduct
from app.application.list_products import ListProducts
from app.infrastructure.db import database_url
from app.infrastructure.product_repository import PostgresProductRepository
from app.infrastructure.products_cache import RedisProductsCache
from app.presentation.health import router as health_router
from app.presentation.products import router as products_router


def create_app(repository: Any | None = None, cache: Any | None = None) -> FastAPI:
    """Composition root. Presentation receives only application use-cases."""
    repository = repository or PostgresProductRepository(database_url())
    cache = cache or RedisProductsCache(os.getenv("REDIS_URL", "redis://redis:6379/0"))
    app = FastAPI(title="Layered Monolith")
    app.state.create_product = CreateProduct(repository, cache)
    app.state.list_products = ListProducts(repository, cache)
    app.include_router(health_router)
    app.include_router(products_router)
    return app


app = create_app()
