#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/7 16:21
# @Author  : JiaYan
# @Site    : 
# @File    : xila_proxy_util.py
# @Software: PyCharm
import requests
from faker import Faker
from lxml import etree
import random

ua = Faker().chrome()
headers = {
    'User-Agent': ua
}
# print('headers = ', headers)

url = 'http://www.xiladaili.com/'


def get_proxies_list():
    proxies_list = []

    try:
        # print(requests.get(url, headers=headers))
        html = requests.get(url, headers=headers).text
        tr_list = etree.HTML(html).xpath('//*[@id="scroll"]/table/tbody/tr')
        # print(tr_list)

        for tr in tr_list:
            ip_port = tr.xpath('./td[1]/text()')
            type_list = tr.xpath('./td[3]/text()')
            proxies = {}
            for t in type_list[0].split(','):
                proxies[t.lower()] = t.lower() + '://' + str(ip_port[0])

            proxies_list.append(proxies)
    except Exception as e:
        print('获取代理ip列表失败, ', e)

    return proxies_list


def get_proxies():
    return random.choice(get_proxies_list())


# if __name__ == '__main__':
#     get_proxies()
