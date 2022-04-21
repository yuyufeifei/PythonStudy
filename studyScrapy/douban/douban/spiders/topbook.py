# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup

from ..items import TopBookItem


class TopbookSpider(scrapy.Spider):
    name = 'topbook'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/top250']

    def parse(self, response):
        # print(response.text)
        bs = BeautifulSoup(response.text, 'html.parser')
        tr_tags = bs.select('tr.item')
        for tr in tr_tags:
            item = TopBookItem()
            name = tr.select_one('div.pl2 a')['title']
            print(name)
            pl = tr.select_one('p.pl').text
            print(pl)
            rate = tr.select_one('span.rating_nums').text
            print(rate)
            inq = tr.select_one('span.inq').text
            print(inq)

            item['name'] = name
            item['pl'] = pl
            item['rate'] = rate
            item['inq'] = inq

            yield item
