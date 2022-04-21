from pyquery import PyQuery as pq
import requests

html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1 class='info bg' float='left'>欢迎</h1>
    <a href='www.baidu.com'>百度</a>
    <h2><!-- 注释 --></h2>
    <div class='info'>111</div>
    <div class='info' float='left'>222</div>
    <div id='gb'>333</div>
    <div><span>444</span></div>
    <div class='info'><span>555</span></div>
    <div id='main'>
        <a href='www.weibo.com'>微博</a>
        <h1>欢迎来到微博</h1>
        div中的文本
    </div>
</body>
</html>
'''

# 创建pyquery对象，实际就是在进行类型转换，将str类型转成PyQuery类型
# 以下是三种创建方式
doc = pq(html)
print(doc)
print(type(doc))
print(doc('title'))

doc2 = pq(url='https://www.baidu.com', encoding='utf-8')
print(doc2)
print(doc2('title'))

doc3 = pq(filename='a.html')
print(doc3)
print(doc3('title'))

# 获取当前节点
print(doc('#main'))
# 获取子节点
print(doc('#main').children())
# 获取父节点
print(doc('#main').parent())
# 获取兄弟节点
print(doc('#main').siblings())
# 获取属性
print(doc('#main>a').attr('href'))
# 获取内容
print(doc('#main').html())
print(doc('#main').text())


# 例
url = 'https://www.qidian.com/rank/yuepiao'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38'}

resp = requests.get(url, headers)
docTemp = pq(resp.text)
names = docTemp('h4>a').text()
print(names)
authors = docTemp('p.author>a.name').text()
print(authors)