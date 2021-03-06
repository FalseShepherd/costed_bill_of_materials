"""empty message

Revision ID: 20e70b3b6dd
Revises: 41b4a992a5c
Create Date: 2015-11-10 19:42:46.999470

"""

# revision identifiers, used by Alembic.
revision = '20e70b3b6dd'
down_revision = '41b4a992a5c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cbom_row', sa.Column('cpn', sa.String(length=50), nullable=True))
    op.add_column('cbom_row', sa.Column('description', sa.String(length=255), nullable=True))
    op.add_column('cbom_row', sa.Column('man_name', sa.String(length=100), nullable=True))
    op.add_column('cbom_row', sa.Column('mpn', sa.String(length=50), nullable=True))
    # manually written sqlite fix :(
    with op.batch_alter_table('cbom_row') as batch_op:
        batch_op.drop_column('int_part_num')
        batch_op.drop_column('man_part_num')



    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cbom_row', sa.Column('man_part_num', sa.VARCHAR(length=50), nullable=True))
    op.add_column('cbom_row', sa.Column('int_part_num', sa.VARCHAR(length=50), nullable=True))
    op.drop_column('cbom_row', 'mpn')
    op.drop_column('cbom_row', 'man_name')
    op.drop_column('cbom_row', 'description')
    op.drop_column('cbom_row', 'cpn')
    op.add_column('cbom', sa.Column('file_name', sa.VARCHAR(length=265), nullable=True))
    ### end Alembic commands ###
