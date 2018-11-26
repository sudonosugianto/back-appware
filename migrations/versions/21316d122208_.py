"""empty message

Revision ID: 21316d122208
Revises: 0875a03a4c83
Create Date: 2018-11-26 14:22:54.522685

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21316d122208'
down_revision = '0875a03a4c83'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stocks', sa.Column('purchaseOrder', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('stocks', 'purchaseOrder')
    # ### end Alembic commands ###