import json

import redis

from app.domain.product import Product


class RedisProductsCache:
    _key = "products:list"

    def __init__(self, url: str) -> None:
        self._client = redis.from_url(url, decode_responses=True)

    def get_products(self) -> list[Product] | None:
        try:
            raw = self._client.get(self._key)
            if raw is None:
                return None
            return [Product(**item) for item in json.loads(raw)]
        except redis.RedisError:
            return None

    def set_products(self, products: list[Product]) -> None:
        try:
            self._client.setex(self._key, 30, json.dumps([{"id": p.id, "name": p.name, "price": p.price} for p in products]))
        except redis.RedisError:
            pass

    def invalidate_products(self) -> None:
        try:
            self._client.delete(self._key)
        except redis.RedisError:
            pass
