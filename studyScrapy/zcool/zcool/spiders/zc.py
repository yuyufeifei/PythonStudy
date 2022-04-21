# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ZcoolItem


class ZcSpider(CrawlSpider):
    name = 'zc'
    allowed_domains = ['zcool.com.cn']
    start_urls = ['https://www.zcool.com.cn/?p=1#tab_anchor']

    rules = (
        Rule(LinkExtractor(allow=r'/?p=\d+#tab_anchor'), follow=True),

        # https://www.zcool.com.cn/work/ZNTkyMjY0OTI=.html
        # 个人感觉 .+ 可以换成 *
        Rule(LinkExtractor(allow=r'/work/.+=.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = ZcoolItem()

        item['image_urls'] = response.xpath('//div[@class="photoInformationContent"]/img/@src').getall()
        item['title'] = response.xpath('//div[@class="contentTitle"]/span/text()').get()

        yield item
