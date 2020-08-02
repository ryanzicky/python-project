import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class VmSpiderSpider(CrawlSpider):
    name = 'vm_spider'
    allowed_domains = ['www.vmgirls.com']
    start_urls = ['http://www.vmgirls.com/']

    rules = (
        Rule(LinkExtractor(allow=r'https://www.vmgirls.com/special/%e8%bd%bb%e7%a7%81%e6%88%bf/'), follow=False),
        # Rule(LinkExtractor(allow=r'https://www.vmgirls.com/\w.html'), callback='parse_item', follow=False),
    )

    def parse(self, response):
        # print('=' * 30)
        # print(response.text)
        # print('=' * 30)
        div_list = response.xpath('/html/body/main/div/div[1]/div')
        print(div_list[0])
        for div in div_list:
            print(div.xpath('./div/div[1]/a/@title'))

    def parse_item(self, response):
        # print('=' * 30)
        # print(response)
        # print('=' * 30)
        div_list = response.xpath('/html/body/main/div/div[2]/div')
        print('=' * 30)
        print(div_list)
        print('=' * 30)
        # item = {}
        # #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # #item['name'] = response.xpath('//div[@id="name"]').get()
        # #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item

    if __name__ == '__main__':
        from scrapy import cmdline

        cmdline.execute('scrapy crawl vm_spider'.split())
