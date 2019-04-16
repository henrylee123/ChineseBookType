# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
from scrapy import Spider
from scrapy.http import Request
from ..items import ChinesebooktypeItem

class gzssztSpider(Spider):

    name = "ChineseBookSpider"
    url = "http://ztflh.xhma.com/html/{num}.html"


    def start_requests(self):
        for num in range(1, 45836):
            yield Request(url=self.url.format(num=str(num)))

    def parse(self, response):
        selector_list = response.xpath("//div[@class='col-xs-12 col-sm-4']/div/a")
        for selector in selector_list:
            items = ChinesebooktypeItem()
            items["title"] = selector.xpath("./@title").extract()[0]
            items["code"] = selector.xpath("./span[1]/text()").extract()[0]
            yield items