#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from yt.models.shema import Channel

"""
File: channel.py
Author: Rafal Marguzewicz
Email: info@pceuropa.net
Github: https://github.com/pceuropa/
Tel: Feel free to contact to me +48 517 777 757
"""


class Channel(Channel):

    def find(self, id: str):
        try:
            return self.execute(f"select channel_id, title, description from {self.table} where id = {id}")
        except Exception:
            return None

    def find_last_id(self):
        try:
            return self.execute(f"select `channel_id` from {self.table} ORDER BY id DESC LIMIT 1")[0]
        except Exception:
            return None

    def find_all_ids(self) -> tuple:
        try:
            return tuple([x[0] for x in self.execute_all(f"select `channel_id` from {self.table}")])
        except Exception:
            return tuple()
