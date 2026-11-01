import psycopg
from psycopg.rows import dict_row

from app.domain.product import Product


class PostgresProductRepository:
    def __init__(self, dsn: str) -> None:
        self._dsn = dsn

    def create(self, product: Product) -> Product:
        with psycopg.connect(self._dsn, row_factory=dict_row) as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO products (name, price) VALUES (%s, %s) RETURNING id, name, price",
                    (product.name, product.price),
                )
                row = cursor.fetchone()
        return Product(id=row["id"], name=row["name"], price=float(row["price"]))

    def list(self) -> list[Product]:
        with psycopg.connect(self._dsn, row_factory=dict_row) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id, name, price FROM products ORDER BY id")
                rows = cursor.fetchall()
        return [Product(id=row["id"], name=row["name"], price=float(row["price"])) for row in rows]
