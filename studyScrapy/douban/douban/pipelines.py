# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import openpyxl


class DoubanPipeline(object):
    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.append(['书名', '出版信息', '评分', '描述'])

    def process_item(self, item, spider):
        line = [item['name'], item['pl'], item['rate'], item['inq']]
        self.ws.append(line)
        # 需要将settings.py中的ITEM_PIPELINES打开才能保存成功
        return item

    def close_spider(self, spider):
        self.wb.save('topbook.xlsx')
        self.wb.close()