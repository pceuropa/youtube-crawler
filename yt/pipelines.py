# -*- coding: utf-8 -*-
from yt.models.movie import Movie


class SqlAlchemy(object):

    def process_item(self, item, spider):
        """Save deals in the database.
        This method is called for every item pipeline component.
        """
        try:
            Movie().insert(item)
        except Exception as e:
            print(e)
