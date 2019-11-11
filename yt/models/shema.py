from scrapy.utils.project import get_project_settings as settings
from yt.logging import logging_slow_query
from sqlalchemy import create_engine, insert, update, Column, CHAR, Date, DateTime, Float, ForeignKey, MetaData, String, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, MEDIUMINT, SMALLINT, TINYINT


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


class Movie(Main):
    table: str = 'movie'
    _table = Table(
        table, metadata,
        Column('id', INTEGER(9), primary_key=True),
        Column('yt_id', String(15, 'utf8_unicode_ci'), nullable=False, unique=True),
        Column('title', String(255, 'utf8_unicode_ci'), nullable=False),
        Column('description', Text(collation='utf8_unicode_ci')),
        Column('tags', Text(collation='utf8_unicode_ci')),
        Column('category', ForeignKey('movie_category.id'), nullable=False, index=True, server_default=text("0")),
        Column('is_family_frendly', TINYINT(1), server_default=text("0")),
        Column('age', TINYINT(1), nullable=False, server_default=text("2")),
        # Column('rank', Float(3)),
        # Column('education', Float(3)),
        Column('effect', Float(3)),
        Column('width', SMALLINT(1)),
        Column('height', SMALLINT(1)),
        Column('language', String(5, 'utf8_unicode_ci')),
        Column('interaction_count', INTEGER(11), nullable=False, server_default=text("0")),
        Column('channel', String(25, 'utf8_unicode_ci')),
        Column('regions_allowed', Text(collation='utf8_unicode_ci')),
        Column('date_published', Date),
        Column('duration', MEDIUMINT(8), nullable=False, server_default=text("0")),
        Column('created', DateTime, server_default=text("current_timestamp()")),
        Column('updated', DateTime)
    )


class Channel(Main):
    table: str = 'channel'
    _table = Table(
        table, metadata,
        Column('channel_id', String(24), primary_key=True, unique=True),
        Column('title', String(100), nullable=False),
        Column('description', Text),
        Column('age', TINYINT(1), server_default=text("9")),
        Column('effect', TINYINT(1), server_default=text("2")),
        Column('language', CHAR(2)),
        Column('tag', String(900), nullable=False),
        Column('category', TINYINT(1)),
        Column('created', DateTime, nullable=False, server_default=text("current_timestamp()")),
        Column('updated', DateTime)
    )


class MovieCategory(Main):
    table: str = 'movie_category'
    _table = Table(
        table, metadata,
        Column('id', TINYINT(2), primary_key=True),
        Column('name', String(255, 'utf8_unicode_ci'), nullable=False),
        Column('safe', TINYINT(1)),
        Column('created', DateTime, server_default=text("current_timestamp()")),
        Column('updated', DateTime)
    )
