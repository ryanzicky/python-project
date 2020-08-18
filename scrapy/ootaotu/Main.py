import requests
from faker import Faker
from lxml import etree
import os

ua = Faker().chrome()
headers = {
    'User-Agent': ua
}

url = 'https://www.ootaotu.com/'


# 解析首页
def parse_first():
    html = requests.get(url, headers=headers)
    response = etree.HTML(html.text)
    li_list = response.xpath('//div[@class="list"]/li')
    for li in li_list:
        detail = {}

        href = li.xpath('./div[@class="img"]/a/@href')[0]
        detail['url'] = url + href
        img_url = li.xpath('./div[@class="img"]/a/span/img/@data-original')[0]
        detail['img_url'] = img_url
        title = li.xpath('./div[@class="tit"]/a/text()')[0]
        detail['title'] = title
        name = li.xpath('./div[@class="if"]/p/span[2]/a/text()')[0]
        detail['name'] = name

        parse_detail(detail)


# 解析明细页
def parse_detail(detail):
    parent_path = os.path.split(os.path.realpath(__file__))[0]
    img_path = os.path.join(parent_path, 'img', detail['name'])
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    html = requests.get(detail['url'], headers=headers)
    response = etree.HTML(html.text)
    image_list = response.xpath('//div[@class="image-list"]/img')
    for img in image_list:
        img_src = img.xpath('./@src')[0]
        img_title = img_src.split('/')[5].split('!')[0]
        download_img(img_src, os.path.join(img_path, img_title))

    next_text = response.xpath('//div[@class="fy"]/a[2]/text()')
    if next_text:
        if next_text[0] != '下一篇':
            next_url = response.xpath('//div[@class="fy"]/a[2]/@href')[0]
            detail['url'] = url + 'tid/' + next_url
            parse_detail(detail)


# 下载图片
def download_img(img_url, img_path):
    r = requests.get(img_url, headers=headers, stream=True)
    if r.status_code == 200 and not os.path.exists(img_path):
        print('下载图片: ', img_path)
        with open(img_path, 'wb') as f:  # 将内容写入图片
            f.write(r.content)


if __name__ == '__main__':
    parse_first()
