import requests

# 不带参数
url = 'http://www.baidu.com'
resp = requests.get(url)
resp.encoding = 'utf-8'
cookie = resp.cookies
headers = resp.headers
print(resp.status_code)
print(cookie)
print(resp.url)
print(headers)
print(resp.text)

# 带参数
url2 = 'https://www.so.com/s'
params = {'q': 'python'}
resp = requests.get(url2, params=params)
resp.encoding = 'utf-8'
print(resp.text)

# 获取json数据
json_data = resp.json()

# 获取图片
url3 = 'https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'
resp = requests.get(url3)
with open('logo.png', 'wb') as file:
    file.write(resp.content)