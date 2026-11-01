from fastapi.testclient import TestClient

from adapters.file.csv_repository import CsvOrderRepository
from adapters.http.app import create_http_app
from core.usecases import CreateOrder, GetOrder


def test_csv_adapter_over_http(tmp_path):
    repository = CsvOrderRepository(str(tmp_path / "orders.csv"))
    client = TestClient(create_http_app(CreateOrder(repository), GetOrder(repository)))
    created = client.post("/orders", json={"sku": "ABC", "qty": 2})
    assert created.status_code == 201
    assert client.get(f"/orders/{created.json()['id']}").json()["sku"] == "ABC"
