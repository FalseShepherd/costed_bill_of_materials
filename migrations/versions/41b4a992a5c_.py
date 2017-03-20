"""empty message

Revision ID: 41b4a992a5c
Revises: 4851774ea63
Create Date: 2015-11-09 12:10:46.995965

"""

# revision identifiers, used by Alembic.
revision = '41b4a992a5c'
down_revision = '4851774ea63'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), nullable=False),
    sa.Column('password', sa.VARCHAR(length=255), nullable=False),
    sa.Column('registered_on', sa.DATETIME(), nullable=False),
    sa.Column('admin', sa.BOOLEAN(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###