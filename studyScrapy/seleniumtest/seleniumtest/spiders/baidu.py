# -*- coding: utf-8 -*-
import scrapy
from scrapy import signals
from selenium.webdriver import Chrome

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.baidu.com/']

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(BaiduSpider, cls).from_crawler(crawler, *args, **kwargs)
        spider.driver = Chrome()
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def spider_closed(self, spider):
        spider.driver.close()
        spider.logger.info('Spider closed: %s', spider.name)

    def parse(self, response):
        print(response.text)
