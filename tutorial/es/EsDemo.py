#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 16:50
# @Author  : JiaYan
# @Site    : 
# @File    : EsDemo.py
# @Software: PyCharm

from elasticsearch import Elasticsearch
from datetime import datetime

es = Elasticsearch([{'host': '47.105.171.231', 'port': 9200}])
result = es.indices.create(index='news', ignore=400)
print(result)