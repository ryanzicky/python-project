#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/4 19:51
# @Author  : JiaYan
# @Site    : 
# @File    : settings.py
# @Software: PyCharm

# -*- coding: utf-8 -*-

# Scrapy settings for step8_king project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

# 1. 爬虫名称
BOT_NAME = 'baidu_spider'

# 2. 爬虫应用路径
SPIDER_MODULES = ['baidu_spider.spiders']
NEWSPIDER_MODULE = 'baidu_spider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# 3. 客户端 user-agent请求头
# USER_AGENT = 'baidu_spider (+http://www.baidu.com)'

# Obey robots.txt rules
# 4. 禁止爬虫配置
# ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 5. 并发请求数
# CONCURRENT_REQUESTS = 4

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 6. 延迟下载秒数
# DOWNLOAD_DELAY = 2


# The download delay setting will honor only one of:
# 7. 单域名访问并发数，并且延迟下次秒数也应用在每个域名
# CONCURRENT_REQUESTS_PER_DOMAIN = 2
# 单IP访问并发数，如果有值则忽略：CONCURRENT_REQUESTS_PER_DOMAIN，并且延迟下次秒数也应用在每个IP
# CONCURRENT_REQUESTS_PER_IP = 3

# Disable cookies (enabled by default)
# 8. 是否支持cookie，cookiejar进行操作cookie
# COOKIES_ENABLED = True
# COOKIES_DEBUG = True

# Disable Telnet Console (enabled by default)
# 9. Telnet用于查看当前爬虫的信息，操作爬虫等...
#    使用telnet ip port ，然后通过命令操作
# TELNETCONSOLE_ENABLED = True
# TELNETCONSOLE_HOST = '127.0.0.1'
# TELNETCONSOLE_PORT = [6023,]


# 10. 默认请求头
# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Accept-Language': 'en',
# }


# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# 11. 定义pipeline处理请求
# ITEM_PIPELINES = {
#    'baidu_spider.pipelines.JsonPipeline': 700,
#    'baidu_spider.pipelines.FilePipeline': 500,
# }


# 12. 自定义扩展，基于信号进行调用
# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#     # 'step8_king.extensions.MyExtension': 500,
# }


# 13. 爬虫允许的最大深度，可以通过meta查看当前深度；0表示无深度
# DEPTH_LIMIT = 3

# 14. 爬取时，0表示深度优先Lifo(默认)；1表示广度优先FiFo

# 后进先出，深度优先
# DEPTH_PRIORITY = 0
# SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleLifoDiskQueue'
# SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.LifoMemoryQueue'
# 先进先出，广度优先

# DEPTH_PRIORITY = 1
# SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleFifoDiskQueue'
# SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.FifoMemoryQueue'

# 15. 调度器队列
# SCHEDULER = 'scrapy.core.scheduler.Scheduler'
# from scrapy.core.scheduler import Scheduler


# 16. 访问URL去重
# DUPEFILTER_CLASS = 'baidu_spider.duplication.RepeatUrl'


# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html

"""
17. 自动限速算法
    from scrapy.contrib.throttle import AutoThrottle
    自动限速设置
    1. 获取最小延迟 DOWNLOAD_DELAY
    2. 获取最大延迟 AUTOTHROTTLE_MAX_DELAY
    3. 设置初始下载延迟 AUTOTHROTTLE_START_DELAY
    4. 当请求下载完成后，获取其"连接"时间 latency，即：请求连接到接受到响应头之间的时间
    5. 用于计算的... AUTOTHROTTLE_TARGET_CONCURRENCY
    target_delay = latency / self.target_concurrency
    new_delay = (slot.delay + target_delay) / 2.0 # 表示上一次的延迟时间
    new_delay = max(target_delay, new_delay)
    new_delay = min(max(self.mindelay, new_delay), self.maxdelay)
    slot.delay = new_delay
"""

# 开始自动限速
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# 初始下载延迟
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# 最大下载延迟
# AUTOTHROTTLE_MAX_DELAY = 10
# The average number of requests Scrapy should be sending in parallel to each remote server
# 平均每秒并发数
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

# Enable showing throttling stats for every response received:
# 是否显示
# AUTOTHROTTLE_DEBUG = True

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings


"""
18. 启用缓存
    目的用于将已经发送的请求或相应缓存下来，以便以后使用【没有网络，但是数据已经缓存下来，可以测试使用】

    from scrapy.downloadermiddlewares.httpcache import HttpCacheMiddleware
    from scrapy.extensions.httpcache import DummyPolicy
    from scrapy.extensions.httpcache import FilesystemCacheStorage
"""
# 是否启用缓存策略
# HTTPCACHE_ENABLED = True

# 缓存策略：所有请求均缓存，下次在请求直接访问原来的缓存即可
# HTTPCACHE_POLICY = "scrapy.extensions.httpcache.DummyPolicy"
# 缓存策略：根据Http响应头：Cache-Control、Last-Modified 等进行缓存的策略
# HTTPCACHE_POLICY = "scrapy.extensions.httpcache.RFC2616Policy"

# 缓存超时时间
# HTTPCACHE_EXPIRATION_SECS = 0

# 缓存保存路径
# HTTPCACHE_DIR = 'httpcache'

# 缓存忽略的Http状态码
# HTTPCACHE_IGNORE_HTTP_CODES = []

# 缓存存储的插件
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

