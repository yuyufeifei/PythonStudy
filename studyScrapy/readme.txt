创建项目：scrapy startproject xxx
进入项目：cd xxx #进入某个文件夹下
创建爬虫：scrapy genspider xxx（爬虫名） xxx.com （爬取域）
生成文件：scrapy crawl xxx -o xxx.json (生成某种类型的文件)
运行爬虫：scrapy crawl XXX
列出所有爬虫：scrapy list
获得配置信息：scrapy settings [options]

scrapy.cfg: 项目的配置文件
tutorial/: 该项目的python模块。在此放入代码（核心）
tutorial/items.py: 项目中的item文件.（这是创建容器的地方，爬取的信息分别放到不同容器里）
tutorial/pipelines.py: 项目中的pipelines文件.
tutorial/settings.py: 项目的设置文件.（我用到的设置一下基础参数，比如加个文件头，设置一个编码）
tutorial/spiders/: 放置spider代码的目录. （放爬虫的地方）

-----------------
之前项目的记录

步骤：
(base) D:\GZH\PycharmProjects>scrapy startproject tutorial
(base) D:\GZH\PycharmProjects>cd tutorial
(base) D:\GZH\PycharmProjects\tutorial>scrapy genspider tieba baidu.com
编写tutorial/items.py tutorial/spiders/tieba.py
(base) D:\GZH\PycharmProjects\tutorial>scrapy crawl tieba -o tiebaitems.json
生成tiebaitems.json
    注：若需生成中文，需在tutorial/settings.py中添加 FEED_EXPORT_ENCODING = 'utf-8'
编写testieba.py查看tiebaitems.json中的内容


XPath Helper Chrome插件

如需使用pipelines需将tutorial/settings.py中的ITEM_PIPELINES放开，然后在tutorial/pipelines.py中编写代码

设置伪装：
    1. 设置代理IP
    2. 设置随机user-agent
如需使用需将tutorial/settings.py中的DOWNLOADER_MIDDLEWARES放开，然后在tutorial/middlewares.py中编写代码
-----------------
yield 用法：
yield item
yield {'title': title, 'content': content}
yield scrapy.Request(next_url, self.parse)

--------
创建CrawlSpider爬虫的语法
scrapy genspider -t crawl [爬虫名] [域名]
使用 -t crawl 指定crawl这个模板

--------
debug
scrapy shell [网址]
之后在命令行中执行代码，例：response.xpath('//div[@id="name"]').get()

--------
getall()与extract()功能相同
get()与extract_first()功能相同
区别：response.xpath('//div[@id="name"]')[0]得到的Selector对象不能使用extract_first()
     response.xpath('//div[@id="name"]')得到的Selector对象列表可使用这4个函数

--------
项目说明：
douban：将数据存储至excel
aixiashu：将数据存至txt文件 yield scrapy.Request
lieyun：将数据存至mysql数据库；使用crawl模板创建爬虫
xsl：模拟登录
zcool：批量下载图片，并修改存储路径
httpua：下载器中间件设置user-agent
seleniumtest：selenium与scrapy结合使用
zufang：将数据存至MongoDB
job：将数据存至MongoDB；使用crawl模板创建爬虫；使用response.css()
doubanredis：从douban复制过来，修改settings.py之后实现分布式，将数据存储至redis
zufangredis：从zufang复制过来，修改settings.py和爬虫文件lianjia.py，将数据存至redis

--------
部署：
1. 在python中安装 twisted scrapy scrapy_redis 等
2. 上传项目至服务器
3. scrapy runspider 爬虫文件    例：scrapy runspider lianjia.py

--------
crawl和runspider的区别：
scrapy crawl：使用spider进行爬取
scrapy runspider：未创建项目的情况下，运行一个编写在Python文件中的spider
