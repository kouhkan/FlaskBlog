"""empty message

Revision ID: a701d7f48728
Revises: 444a9c864dc3
Create Date: 2021-10-18 23:22:37.404423

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a701d7f48728'
down_revision = '444a9c864dc3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tbl_users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.Column('password', sa.String(length=32), nullable=False),
    sa.Column('role', sa.Integer(), nullable=True),
    sa.Column('full_name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=128), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=32), autoincrement=False, nullable=False),
    sa.Column('role', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('full_name', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key')
    )
    op.drop_table('tbl_users')
    # ### end Alembic commands ###
