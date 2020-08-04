# -*- coding: utf-8 -*-
import scrapy


class ZhSpiderSpider(scrapy.Spider):
    name = 'zh_spider'
    allowed_domains = ['zhihu.com']
    # start_urls = ['http://zhihu.com/']
    start_urls = ['https://www.zhihu.com/question/411912384']

    def parse(self, response):
        pass
