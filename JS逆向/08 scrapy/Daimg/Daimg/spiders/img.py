import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


# 获取全站图片并下载
class ImgSpider(CrawlSpider):
    name = "img"
    # allowed_domains = ["www.daimg.com"]
    start_urls = ["http://www.daimg.com/pic/%E6%B1%BD%E8%BD%A6-0-0-0-0-0_1.html"]

    # 匹配页码link 规则
    link = LinkExtractor(allow=r'/pic/%E6%B1%BD%E8%BD%A6-0-0-0-0-0_\d+.html', )
    # 获取每个页面重所有别的img标签信息
    # link2 = LinkExtractor(tags=['img'], attrs=['src'], deny_extensions=[''])
    link2 = LinkExtractor(restrict_xpaths=['/html/body/div[5]/ul/li'], deny_extensions=[''])
    rules = (
        # 配置规则,递归获取所有的页面链接,执行回调函数，获取相应,获取img标签不需要递归，设置follow = false
        Rule(link2, callback='parse_item', follow=False, ),
        Rule(link, follow=True, ),

    )

    def parse_item(self, response):
        print(response.url)
    # def parse(self, response, **kwargs):
    #     pass
