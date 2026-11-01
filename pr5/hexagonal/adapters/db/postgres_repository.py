from uuid import uuid4

import psycopg
from psycopg.rows import dict_row

from core.order import Order


class PostgresOrderRepository:
    def __init__(self, dsn: str) -> None:
        self._dsn = dsn

    def create(self, order: Order) -> str:
        order_id = str(uuid4())
        with psycopg.connect(self._dsn) as conn, conn.cursor() as cur:
            cur.execute("INSERT INTO orders (id, sku, qty) VALUES (%s, %s, %s)", (order_id, order.sku, order.qty))
        return order_id

    def get_by_id(self, order_id: str) -> Order | None:
        with psycopg.connect(self._dsn, row_factory=dict_row) as conn, conn.cursor() as cur:
            cur.execute("SELECT id, sku, qty FROM orders WHERE id = %s", (order_id,))
            row = cur.fetchone()
        return Order(id=row["id"], sku=row["sku"], qty=row["qty"]) if row else None
