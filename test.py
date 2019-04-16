from scrapy import cmdline


if __name__ == "__main__":
    p = 'scrapy crawl ChineseBookSpider'
    cmdline.execute(p.split())
