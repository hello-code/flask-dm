"""empty message

Revision ID: 30214be263a
Revises: 19d1d66da8b
Create Date: 2015-09-11 17:49:36.856408

"""

# revision identifiers, used by Alembic.
revision = '30214be263a'
down_revision = '19d1d66da8b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('material', sa.Column('matnr', sa.String(length=15), nullable=True))
    op.create_unique_constraint(None, 'material', ['matnr'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'material', type_='unique')
    op.drop_column('material', 'matnr')
    ### end Alembic commands ###