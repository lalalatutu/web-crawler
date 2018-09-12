# -*- coding: utf-8 -*-

# Scrapy settings for job51 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'job51'

SPIDER_MODULES = ['job51.spiders']
NEWSPIDER_MODULE = 'job51.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

DOWNLOADER_MIDDLEWARES = {
    # 'Douban.middlewares.DoubanDownloaderMiddleware': 543,
    # 配置随机的浏览器
    'job51.middlewares.RandomMiddleware': 543,
    # 配置随机的代理
    # 'mySpider.middlewares.RandomProxyIpMiddleware': 544,
    # 把系统的默认关闭掉（否则不起作用）
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
}
# -------------------------------------------------------------------
# 不用原来scrapy的去重了，使用自定义的去重过滤器
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 使用自己的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# 是否可以暂停，是否可以继续爬取
SCHEDULER_PERSIST = True
# 优先级队列
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"

# 普通队列
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"

# 栈
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

ITEM_PIPELINES = {
    # 加上爬取时间和爬虫的名称
    'job51.pipelines.ExamplePipeline': 300,

    # 调用系统默认的RedisPipeline，默认把数据存到redis
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

LOG_LEVEL = 'DEBUG'
# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
# DOWNLOAD_DELAY = 1

# 配置主机信息：存储请求request队列，指纹队列,数据队列
REDIS_HOST = "192.168.11.68"
REDIS_PORT = 6379
