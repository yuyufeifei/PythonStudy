# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os.path
from scrapy.pipelines.images import ImagesPipeline


class ZcoolPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        image_requests = super().get_media_requests(item, info)
        for image_request in image_requests:    # 对每个图片下载请求都添加一个item属性
            image_request.item = item
        return image_requests

    def file_path(self, request, response=None, info=None):
        # 重新拼接下载路径
        old_path = super(ZcoolPipeline, self).file_path(request, response, info)
        title = request.item['title']
        new_path = os.path.join('images/', title, old_path.replace('full/', ''))
        return new_path

