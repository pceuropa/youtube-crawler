# -*- coding: utf-8 -*-

from os import environ as env, getcwd, path

path = env.get('PATH_PROJECT') or path.dirname(__file__) or getcwd()

COMMANDS_MODULE = 'yt.commands'

BOT_NAME = 'pceuropa_yt'
SPIDER_MODULES = ['yt.spiders']
NEWSPIDER_MODULE = 'yt.spiders'

# logging level
LOG_LEVEL = 'INFO'

# logging slow query (more than 200ms)
DB_DEBUG = env.get('DB_DEBUG') or True

# show all sql query on console
DB_ECHO = env.get('DB_ECHO') or False
DB_LOGGER = {
    'format': '\n%(asctime)s|%(levelname)-3s|%(message)s',
    'filename': 'sql.log',
    'folder_log': f'{path}/logs/',
    'level': 10
}

# DB SQL
user = env.get('USER_DB') or "root"
password_db = env.get('PASSWORD_DB') or ""
host = env.get('HOST_DB') or "127.0.0.1"
port = env.get('PORT_DB') or "3306"
db_name = env.get('DB_NAME') or "youtube"
CONNECTION_STRING = f"mysql+mysqldb://{user}:{password_db}@{host}:{port}/{db_name}?charset=utf8"

# Scrapy settings for yt project
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'yt (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 28

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16
3
# Disable cookies (enabled by default)
COOKIES_ENABLED = 0
REDIRECT_ENABLED = 0
HTTPPROXY_ENABLED = 0
RETRY_ENABLED = 0
HTTPAUTH_ENABLED = 0
REDIRECT_MAX_TIMES = 2


# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'yt.middlewares.YtSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'yt.middlewares.YtDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'yt.pipelines.SqlAlchemy': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = False
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
