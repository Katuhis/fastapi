"""Create phone number for user column

Revision ID: d666fa7a0dd4
Revises: 
Create Date: 2024-10-21 17:12:55.393964

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd666fa7a0dd4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String, nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'phone_number')