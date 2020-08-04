#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/4 17:42
# @Author  : JiaYan
# @Site    : 
# @File    : ESUtil.py
# @Software: PyCharm

from elasticsearch import Elasticsearch

es = Elasticsearch()


def get_es_index(index_name):
    mapping = {
        'properties': {
            'title': {
                'type': 'text',
                'index': 'not_analyzed'
            }
        }
    }
    if not es.indices.exists(index=index_name):
        es.indices.create(index=index_name, ignore=400)
        es.indices.put_mapping(index=index_name, body=mapping)


def add_data(vm_datas, index_name):
    for data in vm_datas:
        result = search_es_data(index_name, 'title', data['title'])
        if result:
            es_id = result[0]['_id']
            es.index(index=index_name, id=es_id, body=data)
        else:
            es.index(index=index_name, body=data)


def search_es_data(index_name, field_name, field_val):
    query = {
                'query': {
                    'match': {
                        field_name: field_val
                    }
                }
            }

    return es.search(index=index_name, body=query)['hits']['hits']
