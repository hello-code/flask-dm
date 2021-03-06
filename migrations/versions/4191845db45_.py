"""empty message

Revision ID: 4191845db45
Revises: 495abccb4a6
Create Date: 2015-09-11 18:58:17.209696

"""

# revision identifiers, used by Alembic.
revision = '4191845db45'
down_revision = '495abccb4a6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('material', 'matnr',
               existing_type=sa.VARCHAR(length=15),
               type_=sa.String(length=20),
               existing_nullable=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('material', 'matnr',
               existing_type=sa.String(length=20),
               type_=sa.VARCHAR(length=15),
               existing_nullable=True)
    ### end Alembic commands ###
