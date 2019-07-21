from yt.models.shema import Video

"""
File: video.py
Author: Rafal Marguzewicz
Email: info@pceuropa.net
Github: https://github.com/pceuropa/
Tel: Feel free to contact to me +48 517 777 757

Description:
Model Video
    id', INTEGER(9), primary_key=True),
    title', String(255), nullable=False),
    description', Text),
    category', String(55), nullable=False),
    regions_allowed', LONGTEXT),
    education', TINYINT(2), server_default=text("0")),
    fast', TINYINT(1), server_default=text("0")),
    agresion', TINYINT(1)),
    rank', TINYINT(2), server_default=text("0")),
    created', DateTime, server_default=text("current_timestamp()")),
    updated', DateTime),
    image', String(255)),
    url', String(255)),
    yt_id', String(15), nullable=False, unique=True),
    width', INTEGER(11)),
    height', INTEGER(11)),
    content_region', String(5)),
    language', String(5)),
    thumbnail', String(255)),
    is_family_frendly', TINYINT(1)),
    interaction_count', INTEGER(20)),
    date_published', Date),
    channel', String(25)),
    ads', TINYINT(1)),
    locate', String(5)),
    tags', LONGTEXT)
"""


class Video(Video):

    def find(self, id: int):
        try:
            return self.execute(f"select id, title, description from {self.table} where id = {id}")
        except Exception:
            return None

    def find_last_id(self):
        try:
            return self.execute(f"select `yt_id` from {self.table} ORDER BY id DESC LIMIT 1")[0]
        except Exception:
            return None

    def find_all_yt_id(self) -> set:
        try:
            return set(self.execute(f"select GROUP_CONCAT(`yt_id` SEPARATOR ',') from {self.table}")[0].split(','))
        except Exception:
            return set()
