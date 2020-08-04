#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 16:50
# @Author  : JiaYan
# @Site    : 
# @File    : EsDemo.py
# @Software: PyCharm
import time
from elasticsearch import Elasticsearch
from datetime import datetime
import json

'''
Elasticsearch 基本介绍及其与 Python 的对接实现
https://cuiqingcai.com/6214.html
'''

es = Elasticsearch([{'host': '47.105.171.231', 'port': 9200}])
result = es.indices.create(index='news', ignore=400)

# # 创建索引
# es = Elasticsearch([{'host': '47.105.171.231', 'port': 9200}])
# result = es.indices.create(index='news1', ignore=400)
# print(result)
#
# # 删除索引
# es = Elasticsearch([{'host': '47.105.171.231', 'port': 9200}])
# result = es.indices.delete(index='news', ignore=[400, 404])
# print(result)

# 插入数据
# data = {'title': 'Elasticsearch 基本介绍及其与 Python 的对接实现', 'url': 'https://cuiqingcai.com/6214.html'}
# # # 使用create插入数据需要指定id
# result = es.create(index='news', id=1, body=data)
# print(result)

# # 使用index插入数据不需要指定id
# data = {'title': '解决docker安装elasticsearch-head插件请求406问题', 'url': 'https://blog.csdn.net/qq_18361349/article/details/106273684'}
# es.index(index='news', body=data)
# print(result)

# 更新数据
'''
attention that the update API's syntax is different from the create API:
the update_body should be {"doc": data}
index 也可以执行更新操作(没传id就新增并，传了id就更新)
'''

# data = {'title': '解决docker安装elasticsearch-head插件请求406问题', 'url': 'https://blog.csdn.net/qq_18361349/article/details/106273684', 'date': '2020-08-04 14:44:30'}
# result = es.update(index='news', body={"doc": data}, id=1)
# print(result)

# 删除数据
# result = es.delete(index='news', id='7joyuHMBtn559tKX0eJs')
# print(result)


# 查询数据
# 新建一个索引并指定需要分词的字段
# mapping = {
#     'properties': {
#         'title': {
#             'type': 'text',
#             'analyzer': 'ik_max_word',
#             'search_analyzer': 'ik_max_word'
#         }
#     }
# }
#
# es.indices.delete(index='news', ignore=[400, 404])
# es.indices.create(index='news', ignore=400)
# result = es.indices.put_mapping(index='news', body=mapping)
# print(result)
#
# '''
# 这里我们先将之前的索引删除了，然后新建了一个索引，然后更新了它的 mapping 信息，
# mapping 信息中指定了分词的字段，指定了字段的类型 type 为 text，
# 分词器 analyzer 和 搜索分词器 search_analyzer 为 ik_max_word，
# 即使用我们刚才安装的中文分词插件。如果不指定的话则使用默认的英文分词器。
# '''
#
# datas = [
#     {
#         'title': '美国留给伊拉克的是个烂摊子吗',
#         'url': 'http://view.news.qq.com/zt2011/usa_iraq/index.htm',
#         'date': '2011-12-16'
#     },
#     {
#         'title': '公安部：各地校车将享最高路权',
#         'url': 'http://www.chinanews.com/gn/2011/12-16/3536077.shtml',
#         'date': '2011-12-16'
#     },
#     {
#         'title': '中韩渔警冲突调查：韩警平均每天扣1艘中国渔船',
#         'url': 'https://news.qq.com/a/20111216/001044.htm',
#         'date': '2011-12-17'
#     },
#     {
#         'title': '中国驻洛杉矶领事馆遭亚裔男子枪击 嫌犯已自首',
#         'url': 'http://news.ifeng.com/world/detail_2011_12/16/11372558_0.shtml',
#         'date': '2011-12-18'
#     }
# ]
# for data in datas:
#     es.index(index='news', body=data)

# result=es.search(index='news')
# print(result)

dsl = {
    'query': {
        'match': {
            'title': '中国 领事馆'
        }
    }
}
result = es.search(index='news', body=dsl)
print(json.dumps(result, indent=2, ensure_ascii=False))
'''
这里我们使用 Elasticsearch 支持的 DSL 语句来进行查询，使用 match 指定全文检索，检索的字段是 title，内容是“中国领事馆”，搜索结果如下：
'''
'''
{
  "took": 1,
  "timed_out": false,
  "_shards": {
    "total": 5,
    "successful": 5,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": 2,
    "max_score": 2.546152,
    "hits": [
      {
        "_index": "news",
        "_type": "politics",
        "_id": "dk5G9mQBD9BuE5fdHOUm",
        "_score": 2.546152,
        "_source": {
          "title": "中国驻洛杉矶领事馆遭亚裔男子枪击，嫌犯已自首",
          "url": "http://news.ifeng.com/world/detail_2011_12/16/11372558_0.shtml",
          "date": "2011-12-18"
        }
      },
      {
        "_index": "news",
        "_type": "politics",
        "_id": "dU5G9mQBD9BuE5fdHOUj",
        "_score": 0.2876821,
        "_source": {
          "title": "中韩渔警冲突调查：韩警平均每天扣1艘中国渔船",
          "url": "https://news.qq.com/a/20111216/001044.htm",
          "date": "2011-12-17"
        }
      }
    ]
  }
}
'''