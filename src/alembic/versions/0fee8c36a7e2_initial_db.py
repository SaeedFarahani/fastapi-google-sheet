"""initial_db

Revision ID: 0fee8c36a7e2
Revises: 
Create Date: 2021-12-15 12:54:53.749896

"""
from alembic import op
import sqlalchemy as sa

from api.dbutils.database import Base
# revision identifiers, used by Alembic.
revision = '0fee8c36a7e2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=128), nullable=True),
    sa.Column('firstname', sa.String(length=64), nullable=True),
    sa.Column('lastname', sa.String(length=64), nullable=True),
    sa.Column('age', sa.String(length=3), nullable=True),
    sa.Column('nid', sa.String(length=10), nullable=True),
    sa.Column('image', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
