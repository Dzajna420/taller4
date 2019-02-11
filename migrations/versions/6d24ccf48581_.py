"""empty message

Revision ID: 6d24ccf48581
Revises: 377d224cd088
Create Date: 2018-12-19 12:08:11.423284

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d24ccf48581'
down_revision = '377d224cd088'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('replay', sa.Column('likes', sa.Integer(), nullable=True))
    op.drop_column('replay', 'rating')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('replay', sa.Column('rating', sa.FLOAT(), nullable=True))
    op.drop_column('replay', 'likes')
    # ### end Alembic commands ###
