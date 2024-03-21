import scrapy
from scrapy.http import Request
from NewPro.items import NewproItem


class WangyiSpider(scrapy.Spider):
    name = "wangyi"
    allowed_domains = ["www.163.com"]
    start_urls = ["https://news.163.com/"]

    # 定义板块相关的数据结构
    nav_name_dict = {
        '{{__i == 0}}': '要闻',
        '{{__i == 1}}': '上海',
        '{{__i == 2}}': '国内',
        '{{__i == 3}}': '国际',
        '{{__i == 4}}': '独家',
        '{{__i == 5}}': '军事',
    }

    def parse(self, response, **kwargs):
        # 方式一，爬取所有新闻的标题，但是缺少类别以及内容
        # 标签属性为ne-if，包含{{的标签
        # new_title_list = response.xpath('//div[contains(@ne-if,"{{")]/div/a/text()').extract()
        # print(new_title_list)
        # 方式二 爬取板块，以及下面所有的新闻标题、链接

        # 获取所有板块的标签值 ['{{__i == 0}}',  '{{__i == 11}}',...,{{__i == 14}}']
        news_nav_values = response.xpath('//*[contains(@ne-if,"{{")]/@ne-if').extract()
        # 只获取有效的
        for nav in news_nav_values:
            if nav not in self.nav_name_dict:
                continue
            # 根据板块ne-if 属性获取该板块下所有的新闻标题 和链接
            selector_news_list = response.xpath(f'//*[@ne-if="{nav}"]/div/a')
            for select_news in selector_news_list:
                news_title = select_news.xpath('text()').extract_first()
                news_link = select_news.xpath('@href').extract_first()
                # ('3人爬上重庆朝天门大桥顶部"玩心跳" 警方已介入调查', 'https://www.163.com/dy/article/IT63EH1N053469LG.html', '国内')
                # print((news_title, news_link, self.nav_name_dict.get(nav)))

                # 执行请求详情页url
                yield Request(url=news_link, dont_filter=True,
                              callback=self.parse_detail,
                              meta={'news_title': news_title, 'nav_name': self.nav_name_dict.get(nav)}
                              )

    def parse_detail(self, response):
        # 请求详情页
        item = NewproItem()
        news_content_list = response.xpath('//*[@id="content"]/div[@class="post_body"]/p/text()').extract()
        content = ','.join([c.strip() for c in news_content_list])
        news_title = response.meta.get('news_title')
        nav_name = response.meta.get('nav_name')
        item['nav_name'] = nav_name
        item['news_title'] = news_title
        item['content'] = content
        yield item

    def closed(self, spider):
        # self.bro.quit()
        print("此次爬虫全部结束！")
