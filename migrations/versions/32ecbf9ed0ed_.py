"""empty message

Revision ID: 32ecbf9ed0ed
Revises: 
Create Date: 2020-01-08 11:31:46.897494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32ecbf9ed0ed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.String(length=50), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=1000), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('phone_number', sa.String(length=50), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userID', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=50), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['userID'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
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
    op.create_table('subusers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userID', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('apiKey', sa.String(length=100), nullable=False),
    sa.Column('phone_number', sa.String(length=50), nullable=True),
    sa.Column('subuser_type', sa.String(length=50), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['userID'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('suppliers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userSuppliersID', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('phone_number', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.Column('city', sa.String(length=50), nullable=True),
    sa.Column('state', sa.String(length=50), nullable=True),
    sa.Column('zipcode', sa.String(length=50), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['userSuppliersID'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone_number')
    )
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userID', sa.Integer(), nullable=False),
    sa.Column('catID', sa.Integer(), nullable=False),
    sa.Column('item', sa.String(length=50), nullable=False),
    sa.Column('picture', sa.String(length=50), nullable=True),
    sa.Column('size', sa.Integer(), nullable=False),
    sa.Column('unit', sa.String(length=50), nullable=True),
    sa.Column('SKU', sa.Integer(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['catID'], ['category.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['userID'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('packages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('itemID', sa.Integer(), nullable=False),
    sa.Column('userPackageID', sa.Integer(), nullable=False),
    sa.Column('catPackageID', sa.Integer(), nullable=True),
    sa.Column('package_name', sa.String(length=50), nullable=False),
    sa.Column('items_quantity', sa.Integer(), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['catPackageID'], ['category.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['itemID'], ['items.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['userPackageID'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('PO',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('supplierID', sa.Integer(), nullable=False),
    sa.Column('userPOID', sa.Integer(), nullable=False),
    sa.Column('packagePOID', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('buyingPricePerPackage', sa.Float(), nullable=True),
    sa.Column('totalPrice', sa.Float(), nullable=True),
    sa.Column('notes', sa.String(length=255), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['packagePOID'], ['packages.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['supplierID'], ['suppliers.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['userPOID'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('actual_stock',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userActualStocksID', sa.Integer(), nullable=False),
    sa.Column('packageActualStocksID', sa.Integer(), nullable=False),
    sa.Column('actual_stock', sa.Integer(), nullable=True),
    sa.Column('notes', sa.String(length=1000), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['packageActualStocksID'], ['packages.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['userActualStocksID'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sales',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userSalesID', sa.Integer(), nullable=False),
    sa.Column('customerSalesID', sa.Integer(), nullable=False),
    sa.Column('packageSalesID', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('sellingPricePerPackage', sa.Float(), nullable=False),
    sa.Column('totalPrice', sa.Float(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['customerSalesID'], ['customers.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['packageSalesID'], ['packages.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['userSalesID'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('packages_track',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('POID', sa.Integer(), nullable=False),
    sa.Column('salesID', sa.Integer(), nullable=True),
    sa.Column('packageID', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=255), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['POID'], ['PO.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['packageID'], ['packages.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['salesID'], ['sales.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('packages_track')
    op.drop_table('sales')
    op.drop_table('actual_stock')
    op.drop_table('PO')
    op.drop_table('packages')
    op.drop_table('items')
    op.drop_table('suppliers')
    op.drop_table('subusers')
    op.drop_table('customers')
    op.drop_table('category')
    op.drop_table('users')
    # ### end Alembic commands ###
