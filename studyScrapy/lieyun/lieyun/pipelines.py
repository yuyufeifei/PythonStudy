# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi


class LieyunPipeline(object):
    def __init__(self, mysql_config):
        self.dbpool = adbapi.ConnectionPool(
            mysql_config['DRIVER'],
            host=mysql_config['HOST'],
            port=mysql_config['PORT'],
            user=mysql_config['USER'],
            password=mysql_config['PASSWORD'],
            database=mysql_config['DATABASE'],
            # auth_plugin=mysql_config['auth_plugin'],  #mysql8可能会用到
            charset='utf8'
        )

    @classmethod
    def from_crawler(cls, crawler):  # 只要重写了该方法，创建对象时，会调用该方法获取pipeline对象
        mysql_config = crawler.settings['MYSQL_DB_CONFIG']
        return cls(mysql_config)

    def process_item(self, item, spider):
        result = self.dbpool.runInteraction(self.insert_item, item)
        result.addErrback(self.insert_error)
        return item

    def insert_item(self, cursor, item):
        sql = 'insert into pyspider_lieyun(id, title, publish_time, author, content, article_url) values (null, %s, %s, %s, %s, %s)'
        args = (item['title'], item['publish_time'], item['author'], item['content'], item['article_url'])
        cursor.execute(sql, args)

    def insert_error(self, failure):
        print('===============')
        print(failure)
        print('===============')
