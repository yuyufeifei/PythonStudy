from bs4 import BeautifulSoup

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
</body>
</html>
'''

# bs = BeautifulSoup(html, 'html.parser')
bs = BeautifulSoup(html, 'lxml')

# 获取标签
print(bs.title)
print(bs.body)

# 获取标签的属性
print(bs.h1.attrs)

# 获取单个属性
print(bs.h1.get('class'))
print(bs.h1['class'])
print(bs.a['href'])

# 获取标签中的内容
print(bs.a.text)
print(bs.h2.text)
# string可以获取到注释
print(bs.h2.string)

print(bs.find('div', class_='info'))
print(bs.find_all('div', class_='info'))
print(bs.find_all('div', attrs={'float': 'left'}))
print(bs.select('#gb'))
print(bs.select('.info'))
print(bs.select('div>span'))
print(bs.select('div.info>span'))
