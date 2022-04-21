# -*- coding: utf-8 -*-
import scrapy


class XslloginSpider(scrapy.Spider):
    name = 'xsllogin'
    allowed_domains = ['xs6.cc']
    # start_urls = ['http://xs6.cc/']

    # 登录后爬取数据
    # 通过注释start_urls并重写start_requests方法

    def start_requests(self):
        url = '登录url'
        form_data = {
            'username': '',
            'password': '',
            'action': 'login'
        }
        yield scrapy.FormRequest(url, formdata=form_data, callback=self.parse)

    def parse(self, response):
        yield scrapy.Request('登录成功之后的地址', callback=self.parse_response)

    def parse_response(self, response):
        print(response.text)
