"""rm storage type enum

Revision ID: a325a0756797
Revises: 685cb4bc0b79
Create Date: 2021-12-12 22:04:38.060506

"""

# revision identifiers, used by Alembic.
revision = 'a325a0756797'
down_revision = '685cb4bc0b79'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('bundle_store', 'storage_type', type_=sa.String(255), existing_type=sa.Enum("disk", "azure_blob"), nullable=True)
    op.alter_column('bundle_store', 'storage_format', type_=sa.String(255), existing_type=sa.Enum("uncompressed", "compressed_v1"), nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('bundle_store', 'storage_type', type_=sa.Enum("disk", "azure_blob"), existing_type=sa.String(255), nullable=True)
    op.alter_column('bundle_store', 'storage_format', type_=sa.Enum("uncompressed", "compressed_v1"), existing_type=sa.String(255), nullable=True)
    # ### end Alembic commands ###
