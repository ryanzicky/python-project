# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup as Soup


class DbSpiderSpider(scrapy.Spider):
    name = 'db_spider'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        soup = Soup(response.text, 'html.parser')
        ol = soup.find('ol', class_='grid_view')
        li_list = ol.find_all('li')

        for li in li_list:
            # 图片div
            pic_div = li.find('div', class_='pic')
            pic_src = pic_div.find('img')['src']

            # 电影详情div
            info_div = li.find('div', class_='info')
            hd_div = info_div.find_all('div')[0]
            hd_a = hd_div.find('a')
            mv_url = hd_a['href']
            mv_zh_title = hd_a.find_all('span')[0].get_text()
            mv_en_title = hd_a.find_all('span')[1].get_text()
            mv_other_title = hd_a.find('span', class_='other').get_text()

            bd_div = info_div.find_all('div')[1]
            mv_detail = bd_div.find_all('p')[0].get_text()

            star_div = bd_div.find('div', class_='star')
            span_li = star_div.find_all('span')
            rating_num = span_li[1].get_text()
            rate_nums = span_li[3].get_text()

            mv_desc = bd_div.find('p', class_='quote').get_text()
            item = {}

            item['pic_src'] = pic_src
            item['mv_url'] = mv_url
            item['mv_zh_title'] = mv_zh_title
            item['mv_en_title'] = mv_en_title.replace('\xa0', '').replace('/','').replace(' ','')
            item['mv_other_title'] = mv_other_title.replace('\xa0', '').replace('/','').replace(' ','')
            item['mv_detail'] = mv_detail.replace('\n','').replace('\xa0','').replace(' ','')
            item['rating_num'] = rating_num
            item['rate_nums'] = rate_nums
            item['mv_desc'] = mv_desc.replace('\n','').replace(' ','')

            print('item = ', item)
            yield item


        # // *[ @ id = "content"] / div / div[1] / div / div / table[1] / tbody / tr / td[1] / a
        # for tbody in tb_list:
        #     item = {}
        #     mv_title = tbody.xpath('./tr/td[1]/a/@title').extract_first()
        #     mv_url = tbody.xpath('./tr/td[1]/a/@href').extract_first()
        #     mv_type = tbody.xpath('./tr/td[2]/div/a/span/text()').extract_first()
        #     mv_desc = tbody.xpath('./tr/td[2]/div/p/text()').extract_first()
        #     mv_star = tbody.xpath('./tr/td[2]/div/div/span[2]/text()').extract_first()
        #     item['mv_title'] = mv_title
        #     item['mv_url'] = mv_url
        #     item['mv_type'] = mv_type
        #     item['mv_desc'] = mv_desc
        #     item['mv_star'] = mv_star
        #
        #     # print('item = ', item)
        #     yield item

    if __name__ == '__main__':
        from scrapy import cmdline
        cmdline.execute('scrapy crawl db_spider'.split())