# Scrapy settings for douban_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'douban_spider'

SPIDER_MODULES = ['douban_spider.spiders']
NEWSPIDER_MODULE = 'douban_spider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'douban_spider (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 降低并发数，防止被反爬
CONCURRENT_REQUESTS = 2

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 0.1
# 设置2~3秒随机延时
RANDOM_DELAY = [2, 3]
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 6
# CONCURRENT_REQUESTS_PER_IP = 6

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
 'Accept-Encoding': 'gzip, deflate',
 'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
 'Cache-Control': 'no-cache',
 'Connection': 'keep-alive',
 #'Cookie': 'bid=hAoi6-l8I04; douban-fav-remind=1; __utmc=30149280; ll="108288"; __utmc=223695111; __yadk_uid=WHFuqvWTypIoDz9ZmDxvQZcWj8cLp8lO; _vwo_uuid_v2=D947B61D50629F4B949612CE00329AA6C|95f95961588fbff8d028f9385513d4c2; __gads=ID=c971254ae558e718-224c37b6eec400f3:T=1606491258:RT=1606491258:S=ALNI_Maqok3B-GjobYciHC_ijkkoexycgA; ct=y; viewed="34938311"; gr_user_id=057adc8d-7202-4639-a393-db41087a6d94; push_noty_num=0; push_doumail_num=0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1609843363%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.565803361.1605104867.1609739690.1609843363.37; __utmb=30149280.0.10.1609843363; __utmz=30149280.1609843363.37.10.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.1117890868.1606491204.1609739690.1609843363.36; __utmb=223695111.0.10.1609843363; __utmz=223695111.1609843363.36.9.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_id.100001.4cf6=74817fb476940c64.1606491204.36.1609843822.1609740666.',
 'DNT': '1',
 'Host': 'movie.douban.com',
 'Pragma': 'no-cache',
 'Referer': 'https://accounts.douban.com/',
 'Sec-Fetch-Dest': 'document',
 'Sec-Fetch-Mode': 'navigate',
 'Sec-Fetch-Site': 'same-site',
 'Sec-Fetch-User': '?1',
 'Upgrade-Insecure-Requests': '1',
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'douban_spider.middlewares.DoubanSpiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'douban_spider.middlewares.DoubanSpiderDownloaderMiddleware': 543,
    #'douban_spider.middlewares.DoubanSpiderProxyMiddleware': 601,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 455,
    'douban_spider.middlewares.DoubanSpiderRandomDelayMiddleware': 456,
    'douban_spider.middlewares.DoubanSpiderRandomUAMiddleware': 457,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'douban_spider.pipelines.DoubanSpiderPipeline': 300,
   # 'douban_spider.pipelines.MysqlPipeline': 300,
    'douban_spider.pipelines.SqlAlchemyPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# 启用Redis调度存储请求队列
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# 确保所有的爬虫通过Redis去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 允许暂停，Redis数据持久化
SCHEDULER_PERSIST = True

# 默认的请求队列顺序
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"

# 队列形式，请求先进先出
# # SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"

# 栈形式，请求后进先出
# # SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

REDIS_URL = 'redis://localhost:6379'

