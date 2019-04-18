from scrapy import cmdline


if __name__ == "__main__":
    p = 'scrapy crawl ChineseBookSpider_new'
    cmdline.execute(p.split())
