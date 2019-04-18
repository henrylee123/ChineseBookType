# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChinesebooktypeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    fcode = scrapy.Field()
    # name = scrapy.Field()
    ftitle = scrapy.Field()    # name = scrapy.Field()
    flevel = scrapy.Field()    # name = scrapy.Field()
    flastcode = scrapy.Field()    # name = scrapy.Field()
    flasttitle = scrapy.Field()    # name = scrapy.Field()
    furl = scrapy.Field()    # name = scrapy.Field()

