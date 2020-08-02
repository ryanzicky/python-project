import requests

from faker import Faker
from lxml import etree
from proxy_util import get_proxy

url = 'https://www.vmgirls.com/'  # 唯美图片

ua = Faker().chrome()
headers = {'User-Agent': ua}

proxy = get_proxy()
# print(proxy)
proxies = {
    proxy[0:str(proxy).find(':')]: proxy
}


def get_html():
    html = requests.get(url, headers=headers, proxies=proxies)
    response = etree.HTML(html.text)
    # print(response)
    li_list = response.xpath('/html/body/header/nav/div/div/ul/li')

    url_list = []
    for li in li_list:
        href = li.xpath('./a/@href')
        url_list.append(url + str(href[0]))
    print(url_list)


if __name__ == '__main__':
    get_html()