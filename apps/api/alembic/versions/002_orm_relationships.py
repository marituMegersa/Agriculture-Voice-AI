"""Add ORM relationships and foreign key indices

Revision ID: 002_orm_relationships
Revises: None
Create Date: 2026-09-11 08:30:00.000000

"""
from alembic import op
import sqlalchemy as sa

revision = '002_orm_relationships'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_index('ix_agricultural_hubs_coop_id', 'agricultural_hubs', ['cooperative_id'], unique=False)
    op.create_index('ix_extension_agents_hub_id', 'extension_agents', ['hub_id'], unique=False)

def downgrade():
    op.drop_index('ix_extension_agents_hub_id', table_name='extension_agents')
    op.drop_index('ix_agricultural_hubs_coop_id', table_name='agricultural_hubs')
