# import base64
# import io
# from fontTools.ttLib import TTFont
#
# # 58同城网站没有这个了
# font_face = 'base64编码的字符'
# online_face = TTFont(io.BytesIO(base64.b64decode(font_face)))
# print(online_face)

import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
}


def send_request():
    url = 'https://www.shixiseng.com/interns?keyword=%E4%BA%92%E8%81%94%E7%BD%91%2FIT&city=%E5%85%A8%E5%9B%BD&type=intern&from=menu'
    resp = requests.get(url, headers=headers)
    # print(resp.text)
    return resp.text


def parse_html(html):
    bs = BeautifulSoup(html, 'html.parser')
    offers = bs.select('.intern-wrap.intern-item')
    for offer in offers:
        url = offer.select('.f-l.intern-detail__job a')[0]['href']
        print(url)
        parse_detail_url(url)
        break

def parse_detail_url(url):
    resp = requests.get(url, headers=headers)
    bs = BeautifulSoup(resp.text, 'html.parser')
    print(bs.title.text)
    print(bs.select('.com_intro .com-name.com-name--with-label')[0].text.strip())
    print(bs.select('.job-box .job-header .job_msg .job_money.cutom_font')[0].text)


if __name__ == '__main__':
    parse_html(send_request())
