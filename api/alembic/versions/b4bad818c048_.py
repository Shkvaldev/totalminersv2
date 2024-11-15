"""empty message

Revision ID: b4bad818c048
Revises: 4c7bc17b41aa
Create Date: 2024-08-10 10:40:58.102939

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b4bad818c048'
down_revision: Union[str, None] = '4c7bc17b41aa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('miner_items', sa.Column('hosting', sa.Integer(), nullable=True))
    op.add_column('miner_items', sa.Column('income', sa.Integer(), nullable=True))
    op.add_column('miner_items', sa.Column('consumption', sa.Integer(), nullable=True))
    op.add_column('miner_items', sa.Column('profit', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('miner_items', 'profit')
    op.drop_column('miner_items', 'consumption')
    op.drop_column('miner_items', 'income')
    op.drop_column('miner_items', 'hosting')
    # ### end Alembic commands ###
