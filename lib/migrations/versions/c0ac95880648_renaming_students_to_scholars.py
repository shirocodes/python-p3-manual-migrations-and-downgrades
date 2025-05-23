"""Renaming students to scholars

Revision ID: c0ac95880648
Revises: 791279dd0760
Create Date: 2025-05-23 16:27:57.783636

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0ac95880648'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
