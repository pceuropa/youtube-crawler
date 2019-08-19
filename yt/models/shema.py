from scrapy.utils.project import get_project_settings as settings
from yt.logging import logging_slow_query
from sqlalchemy import create_engine, insert, update, Column, Date, DateTime, MetaData, String, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, LONGTEXT, TINYINT

if settings().get("DB_DEBUG"):
    logging_slow_query(settings().get('DB_LOGGER'))

engine = create_engine(settings().get("CONNECTION_STRING"), echo=settings().get("DB_ECHO"))
metadata = MetaData(bind=engine)
connect = engine.connect()

print('\x1b[2j\033c\x1bc')


class Main(object):

    def insert(self, data):
        try:
            insert(self._table).values(data).execute()
        except Exception as e:
            raise e

    def update(self, data={}):
        try:
            update(self._table).values(**data).execute()
        except Exception as e:
            raise e

    def execute(self, sql):
        return connect.execute(text(sql)).fetchone()

    def execute_all(self, sql):
        return connect.execute(text(sql)).fetchall()

    def create_table(self):
        self._table.create(engine, checkfirst=True)

    def drop_table(self):
        self._table.drop(engine, checkfirst=True)

    def truncate_table(self):
        self._table.delete().execute()

    def find_all(self):
        sql = text(f"select * from {self.table}")
        return connect.execute(sql).fetchall()


class Video(Main):
    table: str = 'video'
    _table = Table(
        table, metadata,
        Column('id', INTEGER(9), primary_key=True),
        Column('title', String(255), nullable=False),
        Column('description', Text),
        Column('category', String(55), nullable=False, server_default=text("'None'")),
        Column('regions_allowed', LONGTEXT),
        Column('education', TINYINT(2), server_default=text("0")),
        Column('fast', TINYINT(1), server_default=text("0")),
        Column('agresion', TINYINT(1)),
        Column('rank', TINYINT(2), server_default=text("0")),
        Column('created', DateTime, server_default=text("current_timestamp()")),
        Column('updated', DateTime),
        Column('image', String(255)),
        Column('url', String(255)),
        Column('yt_id', String(15), nullable=False, unique=True),
        Column('width', INTEGER(11)),
        Column('height', INTEGER(11)),
        Column('content_region', String(5)),
        Column('language', String(5)),
        Column('thumbnail', String(255)),
        Column('is_family_frendly', TINYINT(1)),
        Column('interaction_count', INTEGER(25)),
        Column('date_published', Date),
        Column('channel', String(25)),
        Column('ads', TINYINT(1)),
        Column('locate', String(5)),
        Column('tags', LONGTEXT)
    )
