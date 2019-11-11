# -*- coding: utf-8 -*-
from yt.models.movie import Movie
from yt.models.channel import Channel


class SqlAlchemy(object):

    def process_item(self, item, spider):
        """Save deals in the database.
        This method is called for every item pipeline component.
        """
        if spider.name == 'channel':
            self.SaveChannel(item)

        if spider.name == 'youtube':
            self.SaveMovie(item)

    def SaveMovie(self, item):
        try:
            Movie().insert(item)
        except Exception as e:
            print(e)

    def SaveChannel(self, item):
        try:
            Channel().insert(item)
        except Exception as e:
            print(e)
