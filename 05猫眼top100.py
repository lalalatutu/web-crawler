import json
import re
import time
from multiprocessing.pool import Pool

import requests
from requests import RequestException


def savefile(content):
    # item = {}
    # for i in content:
    #     item['a'] = i[0]
    #     item['b'] = i[1]
    #     item['c'] = i[2]
    #     item['d'] = i[3]
    #     item['e'] = i[4]
    #     print(item)

    with open('top.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(dict(content), ensure_ascii=False) + '\n')


def get_content(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException as e:
        print(e)


def parse_content(content):
    pattern = re.compile('<dd>.*?board-index.*?">(\d+)</i>.*?data-src="(.*?)".*?</a>.*?<a[^>]+>(.*?)(?=</a'
                         ').*?star">(.*?)</p>.*?<p[^>]+>(.*?)(?=</p>)', re.S)
    result = re.findall(pattern, content)
    for item in result:
        yield {
            'num': item[0],
            'img': item[1],
            'name': item[2],
            'zhuyan': item[3],
            'shijian': item[4],
        }
    # return result


def main(offset):
    offset = 0
    url = 'http://maoyan.com/board/4?offset={}'.format(offset)
    res = get_content(url)
    for item in parse_content(res):
        savefile(item)


if __name__ == '__main__':
    s=time.time()
    # for i in range(10):
    #     main(i*10)
    pool=Pool()
    pool.map(main,[i*10 for i in range(10)])
    e=time.time()
    print(e-s)

