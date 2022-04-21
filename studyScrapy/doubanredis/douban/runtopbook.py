from scrapy import cmdline

# print('scrapy crawl topbook'.split())
cmdline.execute('scrapy crawl topbook'.split())

# 在终端运行scrapy crawl topbook -o topbook.json 不需要写pipelines 但要在settings.py中设置FEED_EXPORT_ENCODING = 'utf-8'