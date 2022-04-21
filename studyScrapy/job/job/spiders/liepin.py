# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import JobItem


class LiepinSpider(CrawlSpider):
    name = 'liepin'
    allowed_domains = ['liepin.com']
    start_urls = ['https://www.liepin.com/zhaopin/?key=python&currentPage=0']

    rules = (
        Rule(LinkExtractor(allow=r'https://www.liepin.com/zhaopin/?.+key=python&currentPage=\d+.+'), follow=True),
        # 职位链接是两种
        Rule(LinkExtractor(allow=r'https://www.liepin.com/job/\d+\.shtml.*'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'https://www.liepin.com/a/\d+\.shtml.*'), callback='parse_item', follow=False)
    )

    def parse_item(self, response):
        # print(response.xpath('//div[@class="job-detail-box"]/a[1]/@href').getall())

        item = JobItem()
        item['position'] = response.css('.name-box .name.ellipsis-1::text').get()   # 职位
        item['company'] = response.css('.content .name.ellipsis-1::text').get()     # 公司
        item['properties'] = response.css('.job-properties span::text').getall()    # 任职资格
        item['duty'] = response.css('.paragraph dd::text').get()    # 职责
        yield item
