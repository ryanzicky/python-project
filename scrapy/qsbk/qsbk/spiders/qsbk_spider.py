# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class QsbkSpiderSpider(CrawlSpider):
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['http://qiushibaike.com/']


    rules = (
        Rule(LinkExtractor(allow=r'https://www.qiushibaike.com/'), follow=True),
        Rule(LinkExtractor(allow=r'https://www.qiushibaike.com/article/\d'), callback='parse_item', follow=False),

        # Rule(LinkExtractor(allow=r'https://www.qiushibaike.com/article/123439479'), callback='parse', follow=False),
    )

    # def parse(self, response):
    #     print('=' * 30)
    #     # print('response = ', response)
    #     text = response.xpath('//*[@id="single-next-link"]/div/text()').extract()
    #     content = ''
    #     for t in text:
    #         content += t
    #         content += '\n'
    #     print('=' * 30)


    def parse_item(self, response):
        print('=' * 30)
        # print('response = ', response)
        text = response.xpath('//*[@id="single-next-link"]/div/text()').extract()
        content = ''
        for t in text:
            content += t
            content += '\n'

        print('=' * 30)
        yield content

        # item = {}
        # #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # #item['name'] = response.xpath('//div[@id="name"]').get()
        # #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item

    if __name__ == '__main__':
        from scrapy import cmdline
        cmdline.execute('scrapy crawl qsbk_spider'.split())
