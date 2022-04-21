# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient


class ZufangPipeline(object):

    def open_spider(self, spider):
        self.client = MongoClient()     # 默认连接localhost:27017
        self.lianjia = self.client.zufang.lianjia   # 创建文档

    def process_item(self, item, spider):
        self.lianjia.insert_one(dict(item))

    def close_spider(self, spider):
        self.client.close()
