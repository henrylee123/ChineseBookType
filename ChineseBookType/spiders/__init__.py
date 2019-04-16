# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
from scrapy import Spider
from scrapy.http import Request
from ..items import ChinesebooktypeItem

class gzssztSpider(Spider):

    name = "ChineseBookSpider"
    url = "http://ztflh.xhma.com"

    host = "http://ztflh.xhma.com"

    def start_requests(self):
        yield Request(url=self.url)

    def parse(self, response):
            selector_list = response.xpath("//div[@class='col-xs-12 col-sm-4']/div/a")
            for selector in selector_list:
                url = selector.xpath("./@href").extract()[0]
                if (self.host + url) == response.url:
                    raise Exception('haha')
                items = ChinesebooktypeItem()
                items["title"] = selector.xpath("./@title").extract()[0]
                items["code"] = selector.xpath("./span[1]/text()").extract()[0]
                yield items
                yield Request(url=self.host+url, callback=self.parse)
