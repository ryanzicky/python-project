#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/31 16:52
# @Author  : JiaYan
# @Site    : 
# @File    : proxy_utils.py
# @Software: PyCharm

import requests
from faker import Faker
from lxml import etree
import random

# url = 'http://www.xicidaili.com/'
url = 'https://www.kuaidaili.com/free/'

ua = Faker().chrome()
headers = {'User-Agent': ua}


# 获取代理IP列表
def get_proxy_list():
    proxy_list = []
    try:
        html = requests.get(url, headers=headers)
        if html.status_code == 200:
            # print(html.text)
            response = etree.HTML(html.text)
            tr_list = response.xpath('//*[@id="list"]/table/tbody/tr')
            # print(tr_list)

            for tr in tr_list:
                desc = tr.xpath('./td[3]/text()') # ip匿名度
                if desc[0] == '高匿名':
                    ip = tr.xpath('./td[1]/text()')
                    port = tr.xpath('./td[2]/text()')
                    http = tr.xpath('./td[4]/text()')
                    proxy = http[0].lower() + '://' + ip[0] + ':' + port[0]
                    proxy_list.append(proxy)

    except Exception as e:
        print('请求代理服务器失败!,', e)

    return proxy_list


def get_proxy():
    proxy_list = get_proxy_list()
    # print(random.choice(proxy_list))
    return random.choice(proxy_list)


if __name__ == '__main__':
    get_proxy()
