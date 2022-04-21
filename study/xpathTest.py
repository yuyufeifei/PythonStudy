import requests
from lxml import etree

url = 'https://www.qidian.com/rank/yuepiao'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38'}

resp = requests.get(url, headers)
e = etree.HTML(resp.text)

names = e.xpath('//div[@class="book-mid-info"]/h4/a/text()')
authors = e.xpath('//p[@class="author"]/a[1]/text()')
# print(names)
# print(authors)

for name,author in zip(names, authors):
    print(name, ":", author)