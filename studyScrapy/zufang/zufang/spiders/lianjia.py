# -*- coding: utf-8 -*-
import scrapy


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']
    start_urls = [f'https://sjz.lianjia.com/zufang/pg{i}/#contentList' for i in range(1, 3)]

    def parse(self, response):
        urls = ['https://sjz.lianjia.com' + url for url in response.xpath('//p[@class="content__list--item--title"]/a/@href').getall()]
        for url in urls:
            yield scrapy.Request(url, self.parse_info)

    def parse_info(self, response):
        title = response.xpath('//p[@class="content__title"]/text()').get().strip()
        price = response.xpath('//div[@class="content__aside--title"]/span/text()|//div[@class="content__aside--title"]/text()').getall()
        price = ''.join(price).strip().replace('\n', '').replace(' ', '')
        mode = response.xpath('//ul[@class="content__aside__list"]/li[1]/text()').get()     # 租赁方式
        f_type = response.xpath('//ul[@class="content__aside__list"]/li[1]/text()').get()     # 房屋类型
        direction = response.xpath('//ul[@class="content__aside__list"]/li[3]/span[2]/text()').get()   # 朝向
        elevator = response.xpath('//div[@class="content__article__info"]/ul/li[9]/text()').get()   # 电梯
        parking = response.xpath('//div[@class="content__article__info"]/ul/li[11]/text()').get()   # 车位
        water = response.xpath('//div[@class="content__article__info"]/ul/li[12]/text()').get()     # 用水
        electric = response.xpath('//div[@class="content__article__info"]/ul/li[14]/text()').get()  # 用电
        gas = response.xpath('//div[@class="content__article__info"]/ul/li[15]/text()').get()   # 燃气
        heating = response.xpath('//div[@class="content__article__info"]/ul/li[17]/text()').get()  # 暖气

        yield {
            'title': title, 'price': price, 'mode': mode, 'f_type': f_type, 'direction': direction,
            'elevator': elevator, 'parking': parking, 'water': water, 'electric': electric, 'gas': gas,
            'heating': heating
        }
