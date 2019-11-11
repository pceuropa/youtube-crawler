# youtube-crawler
Youtube crawler &amp; scraper based on scrapy. Write in Python3.


REQUIREMENTS
------------
Python 3.6+
SQLAlchemy (optional if save in MariaDB)
Pytest (optional to test unit)

CONFIGURATION
----------
Configuration is in ./yt/settings.py

Default save in CSV. Uncomment yt.pipelines.SqlAlchemy if you need store items in DB
```
ITEM_PIPELINES = {
    # 'yt.pipelines.SqlAlchemy': 300,
    'yt.pipelines.Csv': 300,
}
```

TESTING Model
----------
```
pytest yt/test.py
```
