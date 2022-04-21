import re
import requests

# re.match()
# re.search()
# re.findall()
# re.sub()

url = 'https://www.qiushibaike.com/video/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52'}

resp = requests.get(url, headers=headers)
# print(resp.text)
info = re.findall('<source src="(.*)" type=\'video/mp4\' />', resp.text)
# print(info)

for item in info:
    name = re.findall('com/(.*mp4)', item)[0]
    # print(name)
    respTemp = requests.get('http:' + item, headers=headers)
    # 存在video文件夹下
    with open('video/' + name, 'wb') as file:
        file.write(respTemp.content)
print('视频下载完成！')
