import os
from urllib import parse, request

import requests


def send_request():
    url = "https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page=1&iOrder=0&iSortNumClose=1&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=1650014069369"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
        'referer': 'https://pvp.qq.com/'
    }
    response = requests.get(url, headers=headers)
    return response.json()


def parse_json(json_list):
    result = {}
    data_list = json_list['List']
    for data in data_list:
        # 得到图片url列表
        url_list = parse_url(data)
        # 得到壁纸名称
        name = parse.unquote(data['sProdName'])
        result[name] = url_list
    for item in result:
        print(item, result[item])
    save_image(result)


def parse_url(data):
    url_list = []
    for i in range(1, 9):
        url_list.append(parse.unquote(data[f'sProdImgNo_{i}']).replace('200', ''))
    return url_list


def save_image(data):
    for key in data:
        # 去掉名称中的空格，避免路径有空格
        # dir_path = os.path.join('images', key.replace(' ', ''))
        dir_path = os.path.join('images', key.strip())
        os.mkdir(dir_path)
        for index, url in enumerate(data[key]):
            request.urlretrieve(url, os.path.join(dir_path, f'{index+1}.jpg'))
            print(f'{data[key][index]}下载完毕')


if __name__ == '__main__':
    parse_json(send_request())
