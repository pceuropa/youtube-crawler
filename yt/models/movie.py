#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from yt.models.shema import Movie

"""
File: movie.py
Author: Rafal Marguzewicz
Email: info@pceuropa.net
Github: https://github.com/pceuropa/
Tel: Feel free to contact to me +48 517 777 757
"""


class Movie(Movie):

    def find(self, id: int):
        try:
            return self.execute(f"select id, title, description from {self.table} where id = {id}")
        except Exception:
            return None

    def get_chunk(self, id: int):
        try:
            return self.execute_all(f"select * from {self.table} where id > {id} LIMIT 100")
        except Exception:
            return None

    def find_last_id(self):
        try:
            return self.execute(f"select `yt_id` from {self.table} ORDER BY id DESC LIMIT 1")[0]
        except Exception:
            return None

    def ids(self) -> set:
        try:
            return set([x[0] for x in self.execute_all(f"select `yt_id` from {self.table}")])
        except Exception:
            return set()

    def channel_ids(self) -> tuple:
        try:
            all = set([x[0] for x in self.execute_all(f"SELECT DISTINCT channel FROM {self.table}")])
            saved = set([x[0] for x in self.execute_all(f"SELECT DISTINCT channel_id FROM channel")])
            return all - saved
        except Exception:
            return tuple()

    def detect_language(self, limit: int = 100):
        try:
            return self.execute_all(f"select id, title, description, tags from {self.table} where language IS NULL LIMIT {limit}")
        except Exception:
            return None


if __name__ == '__main__':
    print('echo')
