"""create products table"""

from alembic import op
import sqlalchemy as sa

revision = "0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "products",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.Text(), nullable=False),
        sa.Column("price", sa.Numeric(), nullable=False),
        sa.CheckConstraint("price > 0", name="products_price_positive"),
        sa.CheckConstraint("char_length(name) BETWEEN 1 AND 100", name="products_name_length"),
    )


def downgrade() -> None:
    op.drop_table("products")
