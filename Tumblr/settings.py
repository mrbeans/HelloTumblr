# -*- coding: utf-8 -*-

# Scrapy settings for Tumblr project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Tumblr'

SPIDER_MODULES = ['Tumblr.spiders']
NEWSPIDER_MODULE = 'Tumblr.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Tumblr (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  "Cookie":"rxx=18y86swstpn.12mtbl5c&v=1; _ga=GA1.2.948083063.1522484434; yx=7e5yfo9qops8r%26o%3D3%26f%3Dte; language=%2Czh_CN; _gid=GA1.2.921696942.1534599679; __utma=189990958.948083063.1522484434.1528722653.1534599679.25; __utmb=189990958.0.10.1534599679; __utmc=189990958; __utmz=189990958.1534599679.25.6.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); devicePixelRatio=1; pfp=LTxLMAjH1uVLnBgDwSH9hZfT8bn8V5yMlX9nElRE; pfs=R6sroEOwxQrGd2x9VgBHpqTTlRY; pfe=1542375700; pfu=253133512; logged_in=1; pfx=091eebd0c972adf890d9c5c2e1c75754e45cec3583b2c3cc98c932ba3a26701f%230%236954144258; nts=true; documentWidth=1903; pfg=ba2119f8893f172adaa541ab84503cfeb1625e9476e546a8dd26dbb0f5ff740d%23%7B%22gdpr_is_acceptable_age%22%3A1%2C%22exp%22%3A1566136762%2C%22vc%22%3A%22%22%7D%230903513860; tmgioct=5b78263ac477340737194020; capture=E9XykX5gNwRnfYHv8MVpledXk6U"
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Tumblr.middlewares.TumblrSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Tumblr.middlewares.TumblrDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'Tumblr.pipelines.TumblrPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
