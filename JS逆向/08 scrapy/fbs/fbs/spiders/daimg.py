import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from fbs.items import FbsItem

from scrapy_redis.spiders import RedisCrawlSpider


class DaimgSpider(RedisCrawlSpider):
    name = "daimg"
    # allowed_domains = ["xx.com"]
    # start_urls = ["http://www.daimg.com/pic/%E6%B1%BD%E8%BD%A6-0-0-0-0-0_1.html"]
    redis_key = 'daImgQueue'
    rules = (Rule(LinkExtractor(allow=r"/pic/%E6%B1%BD%E8%BD%A6"), callback="parse_item", follow=True),)

    def parse_item(self, response):
        li_list = response.xpath('/html/body/div[5]/ul/li')
        for li in li_list:
            item = FbsItem()
            title = li.xpath('./a/img/@title').extract_first()
            url = li.xpath('./a/img/@src').extract_first()
            item['title'] = title
            item['url'] = url
            print(item)
            yield item
        # item = {}
        # item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        # item["name"] = response.xpath('//div[@id="name"]').get()
        # item["description"] = response.xpath('//div[@id="description"]').get()
        # return item
