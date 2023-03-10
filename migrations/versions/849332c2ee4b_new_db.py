"""new db

Revision ID: 849332c2ee4b
Revises: 
Create Date: 2023-01-25 13:55:55.181682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '849332c2ee4b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('surname', sa.String(length=32), server_default='Testovidze', nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('quote_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('text', sa.String(length=255), nullable=True),
    sa.Column('rating', sa.Integer(), server_default='1', nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['author_model.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quote_model')
    op.drop_table('author_model')
    # ### end Alembic commands ###
