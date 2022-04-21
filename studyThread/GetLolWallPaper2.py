import os
import threading
from queue import Queue
from urllib import parse, request

import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
    'referer': 'https://pvp.qq.com/'
}


def parse_url(data):
    url_list = []
    for i in range(1, 9):
        url_list.append(parse.unquote(data[f'sProdImgNo_{i}']).replace('200', ''))
    return url_list


class Producer(threading.Thread):
    def __init__(self, page_queue, image_url_queue):
        super().__init__()
        self.page_queue = page_queue
        self.image_url_queue = image_url_queue

    def run(self):
        while not self.page_queue.empty():
            page_url = self.page_queue.get()
            # 访问链接获取数据
            json_list = requests.get(page_url, headers=headers).json()
            # 将数据格式化后，保存图片链接数据，放入队列中
            url_data = {}
            data_list = json_list['List']
            for data in data_list:
                # 得到图片url列表
                url_list = parse_url(data)
                # 得到壁纸名称
                name = parse.unquote(data['sProdName'])
                url_data[name] = url_list

            for key in url_data:
                # 去掉名称中的空格，避免路径有空格
                dir_path = os.path.join('images2', key.strip())
                if not os.path.exists(dir_path):
                    os.mkdir(dir_path)
                for index, url in enumerate(url_data[key]):
                    self.image_url_queue.put({'image_path': os.path.join(dir_path, f'{index + 1}.jpg'), 'image_url': url})


class Customer(threading.Thread):
    def __init__(self, image_url_queue):
        super().__init__()
        self.image_url_queue = image_url_queue

    def run(self):
        while True:
            try:
                image_obj = self.image_url_queue.get(timeout=10)
                request.urlretrieve(image_obj['image_url'], image_obj['image_path'])
                print(f'{image_obj["image_url"]}下载完毕')
            except:
                break


def start():
    total_page = 1  # 29
    page_queue = Queue(total_page)
    image_url_queue = Queue(1000)
    for i in range(total_page):
        page_url = f'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page={i}&iOrder=0&iSortNumClose=1&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=1650014069369'
        # print(page_url)
        page_queue.put(page_url)

    for i in range(5):
        Producer(page_queue, image_url_queue).start()

    for i in range(10):
        Customer(image_url_queue).start()


if __name__ == '__main__':
    start()
