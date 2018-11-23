"""empty message

Revision ID: d2441593dd4c
Revises: 37fdf0c65493
Create Date: 2018-11-23 15:31:28.841382

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2441593dd4c'
down_revision = '37fdf0c65493'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userItem', sa.Integer(), nullable=False),
    sa.Column('catID', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['catID'], ['category.id'], ),
    sa.ForeignKeyConstraint(['userItem'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('items')
    op.drop_table('category')
    # ### end Alembic commands ###
