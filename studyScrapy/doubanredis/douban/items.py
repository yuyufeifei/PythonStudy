# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class TopBookItem(scrapy.Item):
    name = scrapy.Field()
    pl = scrapy.Field()
    rate = scrapy.Field()
    inq = scrapy.Field()