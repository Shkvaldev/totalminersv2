"""empty message

Revision ID: b516407b3e2a
Revises: 9e8e571931f0
Create Date: 2024-10-12 16:22:46.521856

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b516407b3e2a'
down_revision: Union[str, None] = '9e8e571931f0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('image_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'messages', 'images', ['image_id'], ['id'], ondelete='SET NULL')
    op.drop_column('miner_items', 'profit')
    op.drop_column('miner_items', 'hosting')
    op.drop_column('miner_items', 'income')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('miner_items', sa.Column('income', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('miner_items', sa.Column('hosting', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('miner_items', sa.Column('profit', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'messages', type_='foreignkey')
    op.drop_column('messages', 'image_id')
    # ### end Alembic commands ###