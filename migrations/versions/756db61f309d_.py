"""empty message

Revision ID: 756db61f309d
Revises: 9ca218c35089
Create Date: 2018-12-01 15:55:35.419276

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '756db61f309d'
down_revision = '9ca218c35089'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
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
    # ### end Alembic commands ###