"""empty message

Revision ID: 630045d8a70f
Revises: c9373045e68d
Create Date: 2018-11-26 08:43:33.647243

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '630045d8a70f'
down_revision = 'c9373045e68d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userCustomerID', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.String(length=50), nullable=False),
    sa.Column('phoneNumber', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('address', sa.String(length=500), nullable=True),
    sa.Column('city', sa.String(length=50), nullable=True),
    sa.Column('state', sa.String(length=50), nullable=True),
    sa.Column('zipcode', sa.String(length=50), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['userCustomerID'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('sales',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userSalesID', sa.Integer(), nullable=False),
    sa.Column('customerSalesID', sa.Integer(), nullable=False),
    sa.Column('stockSalesID', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('sellingPrice', sa.Float(), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['customerSalesID'], ['customers.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['stockSalesID'], ['stocks.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['userSalesID'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sales')
    op.drop_table('customers')
    # ### end Alembic commands ###