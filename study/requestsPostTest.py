import requests

url = 'https://www.xslou.com/login.php'
data = {'username': '189', 'password': 'mima', 'action': 'login'}
resp = requests.post(url, data=data)
resp.encoding = 'gb2312'
print(resp.status_code)
print(resp.text)

# 使用session
session = requests.session()
resp2 = session.post(url, data=data)
resp2.encoding = 'gb2312'

resp3 = session.get('https://www.xslou.com/modules/article/uservote.php?id=71960')
resp3.encoding = 'gb2312'
print(resp3.text)