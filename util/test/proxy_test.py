#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/7 15:58
# @Author  : JiaYan
# @Site    : 
# @File    : proxy_test.py
# @Software: PyCharm
import requests

from faker import Faker
# from util.proxy_util import get_proxy, get_proxies
from util.xila_proxy_util import get_proxies

# 生成代理
proxies = get_proxies()
print('proxies = ', proxies)

# 生成headers
ua = Faker().chrome()
headers = {
    'User-Agent': ua
}
print('headers = ', headers)

url = 'http://icanhazip.com'

try:
    # response = requests.get(url) #不使用代理
    response = requests.get(url, headers=headers, proxies=proxies)  # 使用代理
    print(response.status_code)
    if response.status_code == 200:
        print(response.text)
except requests.ConnectionError as e:
    print(e.args)