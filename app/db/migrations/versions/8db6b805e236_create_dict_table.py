"""create dict table

Revision ID: 8db6b805e236
Revises: fdf8821871d7
Create Date: 2021-08-20 07:33:31.383880

"""

from alembic import op
import sqlalchemy as sa
from typing import Tuple
from sqlalchemy import func


revision = '8db6b805e236'
down_revision = 'fdf8821871d7'
branch_labels = None
depends_on = None


def timestamps() -> Tuple[sa.Column, sa.Column]:
    return (
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=func.now(),
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=func.now(),
        ),
    )


def create_dicts_table() -> None:
    op.create_table(
        "dicts",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("word", sa.Text, nullable=False, index=True),
        sa.Column("type", sa.Text, nullable=False, index=True),
        sa.Column("fullword", sa.Text),
        sa.Column("content", sa.Text),
        *timestamps(),
    )
    op.execute(
        """
        CREATE TRIGGER update_word_modtime
            BEFORE UPDATE
            ON dicts
            FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column();
        """
    )

def upgrade() -> None:
    create_dicts_table()

def downgrade() -> None:
    op.drop_table("dicts")