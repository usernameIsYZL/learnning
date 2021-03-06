"""empty message

Revision ID: 619d83461cf6
Revises: 8f5c79a727e3
Create Date: 2020-12-25 15:50:48.982004

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '619d83461cf6'
down_revision = '8f5c79a727e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('teacher', sa.Column('cid', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'teacher', 'course', ['cid'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'teacher', type_='foreignkey')
    op.drop_column('teacher', 'cid')
    # ### end Alembic commands ###
