"""second migration

Revision ID: 594c763f3d09
Revises: b72b95ebbd36
Create Date: 2025-04-15 20:48:07.646455

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '594c763f3d09'
down_revision: Union[str, None] = 'b72b95ebbd36'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'hashed_password')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('hashed_password', sa.VARCHAR(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
