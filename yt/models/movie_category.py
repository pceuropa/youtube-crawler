#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from yt.models.shema import MovieCategory

"""
File: movie.py
Author: Rafal Marguzewicz
Email: info@pceuropa.net
Github: https://github.com/pceuropa/
Tel: Feel free to contact to me +48 517 777 757
"""


class MovieCategory(MovieCategory):

    def all_id(self, id: int):
        try:
            return self.execute(f"select id, name from {self.table} where id = {id}")
        except Exception:
            return None

    def all_name(self) -> set:
        try:
            return [x[1] for x in self.execute_all(f"select `id`, `name` from {self.table}")]
        except Exception:
            return []
