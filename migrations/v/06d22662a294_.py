"""empty message

Revision ID: 06d22662a294
Revises: d2441593dd4c
Create Date: 2018-11-23 15:43:51.450057

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06d22662a294'
down_revision = 'd2441593dd4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('category', sa.String(length=50), nullable=True))
    op.add_column('category', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('category', sa.Column('status', sa.Boolean(), nullable=True))
    op.add_column('category', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('category', sa.Column('userItem', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'category', 'items', ['userItem'], ['userItem'])
    op.add_column('items', sa.Column('SKU', sa.Integer(), nullable=True))
    op.add_column('items', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('items', sa.Column('item', sa.String(length=50), nullable=False))
    op.add_column('items', sa.Column('picture', sa.String(length=50), nullable=True))
    op.add_column('items', sa.Column('size', sa.Integer(), nullable=False))
    op.add_column('items', sa.Column('status', sa.Boolean(), nullable=True))
    op.add_column('items', sa.Column('unit', sa.String(length=50), nullable=True))
    op.add_column('items', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('items', 'updated_at')
    op.drop_column('items', 'unit')
    op.drop_column('items', 'status')
    op.drop_column('items', 'size')
    op.drop_column('items', 'picture')
    op.drop_column('items', 'item')
    op.drop_column('items', 'created_at')
    op.drop_column('items', 'SKU')
    op.drop_constraint(None, 'category', type_='foreignkey')
    op.drop_column('category', 'userItem')
    op.drop_column('category', 'updated_at')
    op.drop_column('category', 'status')
    op.drop_column('category', 'created_at')
    op.drop_column('category', 'category')
    # ### end Alembic commands ###
