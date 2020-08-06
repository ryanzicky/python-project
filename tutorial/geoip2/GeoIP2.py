#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/6 11:24
# @Author  : JiaYan
# @Site    : 
# @File    : GeoIP2.py
# @Software: PyCharm

import random
import geoip2.database
"""
https://geoip2.readthedocs.io/en/latest/

"""
reader = geoip2.database.Reader('D:\GeoLite2-City.mmdb')


m = random.randint(0, 255)
n = random.randint(0, 255)
x = random.randint(0, 255)
y = random.randint(0, 255)
randomIP = str(m)+'.'+str(n)+'.'+str(x)+'.'+str(y)
print(randomIP)

response = reader.city(randomIP)
print(response)

