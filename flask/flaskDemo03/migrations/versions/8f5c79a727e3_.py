"""empty message

Revision ID: 8f5c79a727e3
Revises: 613a2d78f511
Create Date: 2020-12-25 14:05:29.044177

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f5c79a727e3'
down_revision = '613a2d78f511'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('isActive', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'isActive')
    # ### end Alembic commands ###
