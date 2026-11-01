"""Run after `docker compose up`; set GATEWAY_URL to override localhost."""
import os
import httpx


def test_catalog_and_orders_through_gateway():
    base = os.getenv("GATEWAY_URL", "http://localhost:8080")
    assert httpx.get(f"{base}/catalog/items").status_code == 200
    response = httpx.post(f"{base}/orders", json={"userId": 1, "itemId": 1, "qty": 1})
    assert response.status_code == 201
    assert "id" in response.json()
