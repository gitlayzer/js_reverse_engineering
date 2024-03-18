import scrapy
from scrapy.http import Request


class SpugSpider(scrapy.Spider):
    name = "spug"
    allowed_domains = ["devops.psi-gene.com"]
    start_urls = ["https://devops.psi-gene.com/api/app/"]

    # 重写start_request 方法，发送post请求，获取cookie
    def start_requests(self):
        # post请求,携带请求体数据
        login_url = 'https://devops.psi-gene.com/api/account/login/'
        # 使用request进行请求
        # 使用Request子类FormRequest进行请求  自动为post请求
        yield scrapy.FormRequest(
            url=login_url,
            formdata={'username': 'admin', 'password': 'Admin@1024', 'type': 'default'},
            callback=self.do_start
        )

    def do_start(self, response):
        '''
                登陆成功后调用parse进行处理
                cookie中间件会帮我们自动处理携带cookie
                '''
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        print(response)
