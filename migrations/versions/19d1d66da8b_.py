"""empty message

Revision ID: 19d1d66da8b
Revises: 2ab666b1e1d
Create Date: 2015-09-11 17:49:09.434849

"""

# revision identifiers, used by Alembic.
revision = '19d1d66da8b'
down_revision = '2ab666b1e1d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('material_matnr_key', 'material', type_='unique')
    op.drop_constraint('material_matnr_key1', 'material', type_='unique')
    op.drop_column('material', 'matnr')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('material', sa.Column('matnr', sa.VARCHAR(length=10), autoincrement=False, nullable=True))
    op.create_unique_constraint('material_matnr_key1', 'material', ['matnr'])
    op.create_unique_constraint('material_matnr_key', 'material', ['matnr'])
    ### end Alembic commands ###
