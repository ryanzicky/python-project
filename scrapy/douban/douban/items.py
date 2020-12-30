# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    pic_src = scrapy.Field()
    mv_url = scrapy.Field()
    mv_zh_title = scrapy.Field()
    mv_en_title = scrapy.Field()
    mv_other_title = scrapy.Field()
    mv_detail = scrapy.Field()
    rating_num = scrapy.Field()
    rate_nums = scrapy.Field()
    mv_desc = scrapy.Field()
