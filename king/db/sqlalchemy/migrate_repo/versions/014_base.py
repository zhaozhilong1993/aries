
"""empty message

Revision ID: 014
Revises:
Create Date: 2016-03-21 11:01:39.317932

"""
import sqlalchemy

# revision identifiers, used by Alembic.
revision = '014'
down_revision = None
branch_labels = None
depends_on = None


def upgrade(migrate_engine):
    meta = sqlalchemy.MetaData()
    meta.bind = migrate_engine

    service = sqlalchemy.Table(
        'service', meta,
        sqlalchemy.Column('id', sqlalchemy.String(36), primary_key=True),
        sqlalchemy.Column('created_at', sqlalchemy.DateTime),
        sqlalchemy.Column('deleted_at', sqlalchemy.DateTime),
        sqlalchemy.Column('updated_at', sqlalchemy.DateTime),
        sqlalchemy.Column('engine_id', sqlalchemy.String(36),
                          nullable=False),
        sqlalchemy.Column('host', sqlalchemy.String(255)),
        sqlalchemy.Column('hostname', sqlalchemy.String(255)),
        sqlalchemy.Column('process', sqlalchemy.String(255)),
        sqlalchemy.Column('topic', sqlalchemy.String(255)),
        sqlalchemy.Column('report_interval', sqlalchemy.String(255)),
        mysql_engine='InnoDB',
        mysql_charset='utf8',
    )

    account = sqlalchemy.Table(
        'account', meta,
        sqlalchemy.Column('id', sqlalchemy.String(36), primary_key=True),
        sqlalchemy.Column('created_at', sqlalchemy.DateTime),
        sqlalchemy.Column('deleted_at', sqlalchemy.DateTime),
        sqlalchemy.Column('updated_at', sqlalchemy.DateTime),
        sqlalchemy.Column('username', sqlalchemy.String(36), nullable=False),
        sqlalchemy.Column('user_password', sqlalchemy.String(255), nullable=False),
        sqlalchemy.Column('user_id', sqlalchemy.String(255), nullable=False),
        sqlalchemy.Column('project_id', sqlalchemy.String(255), nullable=False),
        sqlalchemy.Column('cloud_type', sqlalchemy.String(36), nullable=False),
        mysql_engine='InnoDB',
        mysql_charset='utf8',
    )

    tables = (
        service,
        account,
    )

    for index, table in enumerate(tables):
        try:
            table.create()
        except Exception:
            # If an error occurs, drop all tables created so far to return
            # to the previously existing state.
            meta.drop_all(tables=tables[:index])
            raise
