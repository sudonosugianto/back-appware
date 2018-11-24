"""empty message

Revision ID: 37fdf0c65493
Revises: 113548866db9
Create Date: 2018-11-23 15:21:51.105030

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37fdf0c65493'
down_revision = '113548866db9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userItem', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['userItem'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('items')
    # ### end Alembic commands ###