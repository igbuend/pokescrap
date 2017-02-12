# -*- coding: utf-8 -*-
"""Scrapy settings for pokescrap project"""
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html


# Configure which map to process.
# Maps using the same software as "sgpokemap.com" should work out-of-the-box
# Please refer to maps at https://www.jeerbees.com/pokemon/city-wide-pokemon-scanners/

POKESCRAP_SCOPE = 'http://sgpokemap.com/'

# You have to determine the boundaries of the rectangle to be scraped
# Do not make this too big
# Finding coordinates: go to Google Maps, click on the location
# choose two points of a rectangle
# string = latitude1,latitude2,longitude1,longitude2

POKESCRAP_BOUNDS = "103.91523599624634,103.94111394882204,1.328325473117126,1.3367989613576803"

# Path to SQLite database where results are stored

POKESCRAP_DB = "db/pokescrap.sqlite"

BOT_NAME = 'pokescrap'

SPIDER_MODULES = ['pokescrap.spiders']
NEWSPIDER_MODULE = 'pokescrap.spiders'

# In case of problems with the "Twisted" module and HTTPS connections
# try the following.
#   refer to https://doc.scrapy.org/en/latest/topics/settings.html
#   try sudo -H pip install --upgrade Twisted
#   possible values: "TLS", "TLSv1.0", "TLSv1.1", "TLSv1.2", "SSLv3"

DOWNLOADER_CLIENT_TLS_METHOD = "TLS"

## default = DEBUG, other possibilities are CRITICAL, ERROR, WARNING, INFO and DEBUG
LOG_LEVEL = 'INFO'

## after initial tests, put this to '0' to disable logging

LOG_ENABLED = '1'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# Pokescrap will use this (very common) USER_AGENT for requests
# next version will use a randomised USER-AGENT to prevent blocking

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'

# Pokescrap does not obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# Since Pokescrap is not a spider, in reality this will be "1"

CONCURRENT_REQUESTS = 4

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'pokescrap.middlewares.PokescrapSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'pokescrap.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# Pokescrap: do not disable

ITEM_PIPELINES = {
    'pokescrap.pipelines.PokescrapPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

## Added by pokeman (https://www.jeerbees.com) for supporting a list of proxies
## Please refer to https://github.com/aivarsk/scrapy-proxies
## install with "sudo pip install scrapy_proxies"

# Retry many times since proxies often fail
# RETRY_TIMES = 10
# Retry on most error codes since proxies fail for different reasons
#RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]
#
#DOWNLOADER_MIDDLEWARES = {
#    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
#    'scrapy_proxies.RandomProxy': 100,
#    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
#}

# Proxy list containing entries like
# http://host1:port
# http://username:password@host2:port
# http://host3:port
# ...
#PROXY_LIST = 'proxylist.txt'

# Proxy mode
# 0 = Every requests have different proxy
# 1 = Take only one proxy from the list and assign it to every requests
# 2 = Put a custom proxy to use in the settings
#PROXY_MODE = 2

# If proxy mode is 2 uncomment this sentence :
#CUSTOM_PROXY = "http://127.0.0.1:8080"

