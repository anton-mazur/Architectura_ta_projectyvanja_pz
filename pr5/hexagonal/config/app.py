import os

from adapters.db.postgres_repository import PostgresOrderRepository
from adapters.file.csv_repository import CsvOrderRepository
from adapters.http.app import create_http_app
from core.usecases import CreateOrder, GetOrder


def build_app():
    adapter = os.getenv("REPO_ADAPTER", "db")
    if adapter == "file":
        repository = CsvOrderRepository(os.getenv("CSV_PATH", "/data/orders.csv"))
    elif adapter == "db":
        dsn = "postgresql://{user}:{password}@{host}:{port}/{name}".format(
            user=os.getenv("DB_USER", "orders"), password=os.getenv("DB_PASS", "orders"),
            host=os.getenv("DB_HOST", "db"), port=os.getenv("DB_PORT", "5432"), name=os.getenv("DB_NAME", "orders"),
        )
        repository = PostgresOrderRepository(dsn)
    else:
        raise RuntimeError("REPO_ADAPTER must be db or file")
    return create_http_app(CreateOrder(repository), GetOrder(repository))


app = build_app()
