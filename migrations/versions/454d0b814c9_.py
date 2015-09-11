"""empty message

Revision ID: 454d0b814c9
Revises: 4191845db45
Create Date: 2015-09-11 18:58:45.218243

"""

# revision identifiers, used by Alembic.
revision = '454d0b814c9'
down_revision = '4191845db45'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('material', 'matnr',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=15),
               existing_nullable=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('material', 'matnr',
               existing_type=sa.String(length=15),
               type_=sa.VARCHAR(length=20),
               existing_nullable=True)
    ### end Alembic commands ###
