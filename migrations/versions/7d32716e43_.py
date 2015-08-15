"""empty message

Revision ID: 7d32716e43
Revises: 1e377573b03
Create Date: 2015-08-15 23:06:56.042510

"""

# revision identifiers, used by Alembic.
revision = '7d32716e43'
down_revision = '1e377573b03'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('material', sa.Column('name', sa.String(length=255), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('material', 'name')
    ### end Alembic commands ###
