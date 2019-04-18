# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
from scrapy import Spider
from scrapy.http import Request
from ..items import ChinesebooktypeItem

class gzssztSpider(Spider):

    name = "ChineseBookSpider_new"
    url = "http://ztflh.xhma.com"

    host = "http://ztflh.xhma.com"

    def start_requests(self):
        meta={"flevel": "0", "ftitle": "", "fcode": ""}
        yield Request(url=self.url, meta=meta)

    def parse(self, response):
            selector_list = response.xpath("//div[@class='col-xs-12 col-sm-4']/div/a")
            if not selector_list:
                msg = f"rerequests: {response.url}"
                print(msg)
                yield Request(response.url, meta=response.meta, callback=self.parse, dont_filter=True)
            else:
                for selector in selector_list:
                    url = selector.xpath("./@href").extract()[0]
                    if (self.host + url) == response.url:
                        msg = f'haha: end {response.url}'
                        print(msg)
                    else:
                        items = ChinesebooktypeItem()
                        title = selector.xpath("./@title").extract()[0]
                        items["ftitle"] = title
                        code = selector.xpath("./span[1]/text()").extract()[0]
                        items["fcode"] = code
                        items["flastcode"] = response.meta["fcode"]
                        items["flasttitle"] = response.meta["ftitle"]
                        level = str(int(response.meta["flevel"]) + 1)
                        items["flevel"] = level
                        items["furl"] = url

                        yield items

                        meta = {"flevel": level, "ftitle": title, "fcode": code}
                        yield Request(url=self.host+url, callback=self.parse, meta=meta)
