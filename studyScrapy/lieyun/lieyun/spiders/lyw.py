# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import LieyunItem


class LywSpider(CrawlSpider):
    name = 'lyw'
    allowed_domains = ['lieyunwang.com']
    start_urls = ['https://www.lieyunwang.com/latest/p1.html']

    rules = (
        Rule(LinkExtractor(allow=r'/latest/p\d+.html'), follow=True),
        Rule(LinkExtractor(allow=r'/archives/\d+'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        # item = {}
        # #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # #item['name'] = response.xpath('//div[@id="name"]').get()
        # #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item

        print(response.url)

        item = LieyunItem()

        item['title'] = response.xpath('//h1[@class="lyw-article-title-inner"]/text()').getall().pop().strip()
        item['publish_time'] = response.xpath('//h1[@class="lyw-article-title-inner"]/span/text()').get()
        item['author'] = response.xpath('//a[@class="author-name open_reporter_box"]/text()').get()
        # response.xpath('//a[contains(@class,"author-name")]/text()').get()
        item['content'] = ''.join(response.xpath('//div[@id="main-text-id"]//*').getall()).strip()  # 带html标签
        # content = ''.join(response.xpath('//div[@id="main-text-id"]//text()').getall()).strip()   # 不带html标签
        item['article_url'] = response.url

        yield item
