# -*- coding: utf-8 -*-
import scrapy


class TbyzSpider(scrapy.Spider):
    name = 'tbyz'
    allowed_domains = ['aixiawx.com']
    start_urls = ['https://www.aixiawx.com/36/36731/16900859.html']

    def parse(self, response):
        title = response.xpath('//div[@class="bookname"]/h1/text()').extract_first().strip()
        content = response.xpath('string(//div[@id="content"])').extract_first().strip().replace('\xa0', '')
        # print(title)
        # print(content)
        yield {
            'title': title,
            'content': content
        }
        next_url = response.xpath('//div[@class="bottem1"]/a/@href').extract()[3]
        # print(next_url)
        if next_url.endswith('html'):
            next_url = 'https://www.aixiawx.com' + next_url
            yield scrapy.Request(next_url, self.parse)
