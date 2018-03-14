import json
import requests
from requests.exceptions import RequestException
from MaoyanTop100.useragent import get_useragent
import re
import threading


# 获取单个url的源文件
def get_one_page(url, headers):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


# 正则解析页面
def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)</a>'
                         '.*?star.*?>(.*?)</p>.*?releasetime">(.*?)</p>'
                         '.*?integer">(.*?)</i>.*?fraction">(\d+)</i>.*?</dd>', re.S)

    items = re.findall(pattern, html)  # items 是列表 ，元素是原组

    # 迭代器 返回字典
    for item in items:
        yield {
            'index': item[0],
            'image_link': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }


def write_to_file(content):
    with open('result.txt', 'a', encoding='UTF-8') as f:
        # json.dumps 是将字典转换成sr
        f.write(json.dumps(content, ensure_ascii=False) + '\n')  # 写入文件乱码：需要指定 open 和 json中的编码
        f.close()


def main(offset):
    url = "http://maoyan.com/board/4?offset=" + str(offset) # 添加offset 批量抓取页面
    headers = {"User-Agent": get_useragent()}  # 随机取得useragent

    html = get_one_page(url, headers)
    for item in parse_one_page(html):  # 迭代器返回字典，
        write_to_file(item)  # 将迭代器返回值 用json解析为字符串
        print(item)


if __name__ == '__main__':
    for i in range(10):
        main(i*10)

    # 使用线程池，但是有个问题，不是按照顺序抓取的
    # pool = Pool()
    # pool.map(main,[i*10 for i in range(10)])