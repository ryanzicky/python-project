# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from elasticsearch import Elasticsearch

# 初始化es连接并创建索引
es = Elasticsearch([{'host': '47.105.171.231', 'port': 9200}])
if not es.indices.exists(index='douban_movie'):
    es.indices.create(index='douban_movie', ignore=400)


class DoubanPipeline(object):

    def process_item(self, item, spider):
        # print('item ===== ', item)
        result = es.index(index='douban_movie', body=item)
        print(result)
        return item
