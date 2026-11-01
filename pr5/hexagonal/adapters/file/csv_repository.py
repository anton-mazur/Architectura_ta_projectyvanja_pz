import csv
import os
from pathlib import Path
from threading import Lock
from uuid import uuid4

from core.order import Order


class CsvOrderRepository:
    def __init__(self, path: str) -> None:
        self._path = Path(path)
        self._lock = Lock()

    def _ensure_file(self) -> None:
        self._path.parent.mkdir(parents=True, exist_ok=True)
        if not self._path.exists():
            with self._path.open("w", newline="", encoding="utf-8") as f:
                csv.writer(f).writerow(["id", "sku", "qty"])

    def create(self, order: Order) -> str:
        order_id = str(uuid4())
        with self._lock:
            self._ensure_file()
            with self._path.open("a", newline="", encoding="utf-8") as f:
                csv.writer(f).writerow([order_id, order.sku, order.qty])
        return order_id

    def get_by_id(self, order_id: str) -> Order | None:
        with self._lock:
            self._ensure_file()
            with self._path.open(newline="", encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    if row["id"] == order_id:
                        return Order(id=row["id"], sku=row["sku"], qty=int(row["qty"]))
        return None
