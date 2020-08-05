# -*- coding: utf-8 -*-
import scrapy


class DbSpiderSpider(scrapy.Spider):
    name = 'db_spider'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/chart']

    def parse(self, response):
        tb_list = response.xpath('//*[@id="content"]/div/div[1]/div/div/table')
        # print('tb_list = ', tb_list)

        # // *[ @ id = "content"] / div / div[1] / div / div / table[1] / tbody / tr / td[1] / a
        for tbody in tb_list:
            item = {}
            mv_title = tbody.xpath('./tr/td[1]/a/@title').extract_first()
            mv_url = tbody.xpath('./tr/td[1]/a/@href').extract_first()
            mv_type = tbody.xpath('./tr/td[2]/div/a/span/text()').extract_first()
            mv_desc = tbody.xpath('./tr/td[2]/div/p/text()').extract_first()
            mv_star = tbody.xpath('./tr/td[2]/div/div/span[2]/text()').extract_first()
            item['mv_title'] = mv_title
            item['mv_url'] = mv_url
            item['mv_type'] = mv_type
            item['mv_desc'] = mv_desc
            item['mv_star'] = mv_star

            # print('item = ', item)
            yield item

    if __name__ == '__main__':
        from scrapy import cmdline
        cmdline.execute('scrapy crawl db_spider'.split())