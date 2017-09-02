import scrapy

class BaiduSpider(scrapy.spiders.Spider):
    name         = "baidu"
    allow_domain = ["http://www.baidu.com", "http://news.baidu.com"]
    start_url    = ["http://news.baidu.com/"]
    def parse(self, response):
        current_url  = response.url
        body         = response.body
        unicode_body = response.body_as_unicode()
