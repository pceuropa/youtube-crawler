# -*- coding: utf-8 -*-
import csv
from yt.models.movie import Movie
from yt.models.channel import Channel
from os import path


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


class Csv(object):

    def process_item(self, item, spider):
        """Save deals in the database.
        This method is called for every item pipeline component.
        """
        filename = 'movie.csv'
        file_exists = path.isfile(filename)

        with open(filename, 'a+') as f:  # Just use 'w' mode in 3.x
            w = csv.DictWriter(f, item.keys())
            if not file_exists:
                w.writeheader()  # file doesn't exist yet, write a header
            w.writerow(item)
