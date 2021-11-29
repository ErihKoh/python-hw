"""fifth migration

Revision ID: d39bb29de0e1
Revises: 2de18401c222
Create Date: 2021-11-29 11:30:00.132452

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd39bb29de0e1'
down_revision = '2de18401c222'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contact_address')
    op.drop_table('contact_email')
    op.drop_table('contact_phone')
    op.add_column('contact', sa.Column('phone_id', sa.Integer(), nullable=True))
    op.add_column('contact', sa.Column('email_id', sa.Integer(), nullable=True))
    op.add_column('contact', sa.Column('address_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'contact', 'address', ['address_id'], ['id'])
    op.create_foreign_key(None, 'contact', 'phone', ['phone_id'], ['id'])
    op.create_foreign_key(None, 'contact', 'email', ['email_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'contact', type_='foreignkey')
    op.drop_constraint(None, 'contact', type_='foreignkey')
    op.drop_constraint(None, 'contact', type_='foreignkey')
    op.drop_column('contact', 'address_id')
    op.drop_column('contact', 'email_id')
    op.drop_column('contact', 'phone_id')
    op.create_table('contact_phone',
    sa.Column('contact_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('phone_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['contact_id'], ['contact.id'], name='contact_phone_contact_id_fkey'),
    sa.ForeignKeyConstraint(['phone_id'], ['phone.id'], name='contact_phone_phone_id_fkey')
    )
    op.create_table('contact_email',
    sa.Column('contact_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('email_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['contact_id'], ['contact.id'], name='contact_email_contact_id_fkey'),
    sa.ForeignKeyConstraint(['email_id'], ['email.id'], name='contact_email_email_id_fkey')
    )
    op.create_table('contact_address',
    sa.Column('contact_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('address_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['address_id'], ['address.id'], name='contact_address_address_id_fkey'),
    sa.ForeignKeyConstraint(['contact_id'], ['contact.id'], name='contact_address_contact_id_fkey')
    )
    # ### end Alembic commands ###