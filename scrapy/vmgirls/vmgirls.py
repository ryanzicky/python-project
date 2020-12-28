import requests

from faker import Faker
from lxml import etree
from util.proxy_util import get_proxy
from util.ESUtil import *
import time

url = 'https://www.vmgirls.com/'  # 唯美图片

ua = Faker().chrome()
headers = {'User-Agent': ua}

proxy = get_proxy()
proxies = {
    proxy[0:str(proxy).find(':')]: proxy
}

date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def get_html():
    html = requests.get(url, headers=headers, proxies=proxies)
    response = etree.HTML(html.text)
    li_list = response.xpath('/html/body/header/nav/div/div/ul/li')

    url_list = []
    for li in li_list:
        title = li.xpath('./a/text()')
        href = li.xpath('./a/@href')
        if href[0] == '/':
            vm_url = {'title': title[0], 'url': url, 'date': date}
            url_list.append(vm_url)
        elif 'https://' in href[0]:
            vm_url = {'title': title[0], 'url': str(href[0]), 'date': date}
            url_list.append(vm_url)
        else:
            vm_url = {'title': title[0], 'url': url + str(href[0]), 'date': date}
            url_list.append(vm_url)

    get_es_index('vmgirls') # 判断索引是否存在
    add_data(url_list, 'vmgirls') # 插入es数据


if __name__ == '__main__':
    get_html()