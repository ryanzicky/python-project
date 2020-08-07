#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/31 15:45
# @Author  : JiaYan
# @Site    : 
# @File    : Main.py
# @Software: PyCharm

import requests
from faker import Faker
from lxml import etree
from utils.proxy_util import get_proxy

# url = 'http://www.baidu.com'
# url = 'https://www.vmgirls.com/' # 唯美图片
# url = 'https://satori.mycard.moe/photos' # 女装大佬
url = 'https://github.com/komeiji-satori/Dress'  # 女装大佬github

base_url = 'https://github.com/'

ua = Faker().chrome()
headers = {'User-Agent': ua}

proxy = get_proxy()
# print(proxy)
proxies = {
    proxy[0:str(proxy).find(':')]: proxy
}


# print(proxies)

def get_dic_list():
    try:
        html = requests.get(url, headers=headers, proxies=proxies)
        # html = requests.get(url, headers=headers)
        # print(html)

        response = etree.HTML(html.text)
        # print(response)

        div_list = response.xpath('//*[@id="js-repo-pjax-container"]/div[2]/div/div[2]/div[1]/div[2]/div[3]/div[1]/div')
        # print(div_list)

        dic_list = []
        for div in div_list:
            dic_url = div.xpath('./div[2]/span/a/@href')
            # print(dic_url)

            if dic_url:
                dic_list.append(str(base_url) + dic_url[0])

        return dic_list

    except Exception as e:
        print('获取文件夹路径失败!, ', e)

    return []


def get_img_list():
    try:
        dic_list = get_dic_list()
        # for dic in dic_list:
        #     print(dic)
        dic_url = dic_list[2]
        html = requests.get(dic_url, headers=headers, proxies=proxies)
        response = etree.HTML(html.text)
        div_list = response.xpath('//*[@id="js-repo-pjax-container"]/div[2]/div/div[3]/div[3]/div/div')

        img_list = []
        for div in div_list:
            href = div.xpath('./div[2]/span/a/@href')
            title = div.xpath('./div[2]/span/a/text()')
            if title:
                img_list.append(base_url + href[0])

        return img_list
    except Exception as e:
        print('获取图片路径失败!, ', e)

    return []


def get_img():
    img_list = get_img_list()
    # print(img_list)
    for img_url in img_list:
        html = requests.get(img_url, headers=headers, proxies=proxies)
        response = etree.HTML(html.text)
        src = response.xpath('/html/body/div[4]/div/main/div[2]/div/div[3]/div[2]/div/span/img/@src')
        print(base_url + src[0])


if __name__ == '__main__':
    get_img()
