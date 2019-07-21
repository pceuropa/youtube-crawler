# -*- coding: utf-8 -*-
from yt.models.video import Video


class SqlAlchemy(object):

    def process_item(self, item, spider):
        """Save deals in the database.
        This method is called for every item pipeline component.
        """
        try:
            Video().insert(item)
            print(f'inserted {item["yt_id"]}')
        except Exception as e:
            print()
            print(e)
