import json
import os
import re
from urllib.parse import urlencode

import requests
headers = {
    # 'Referer': 'https://www.toutiao.com/a6604036734025990664/',
    # 'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
    # 'X-DevTools-Emulate-Network-Conditions-Client-Id': '715B2F3A92C4628413D0059AA7091801'
}
for i in range(20):
    offset=(i*20)
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab'
    }
    url = 'https://www.toutiao.com/search_content/?'+urlencode(data)
    response = requests.get(url)
    content = response.text
    # print(content)
    # 方法1，使用正则匹配到所有文章的链接
    partten=re.compile('(?<="article_url": )"(.*?)",',re.S)
    article_urls=re.findall(partten,content)

    # 方法2，使用字典提取json数据中的链接
    # content=json.loads(content)
    # datas=content['data']
    # for data in datas:
    #     article_urls = data.get('article_url')
    #     print(article_urls)
    path='./data/image/'
    if not os.path.exists(path):
        os.makedirs(path)
    def saveimg(image_url):
        print(image_url)
        response=requests.get(image_url)
        cont=response.content
        pa = image_url.split("/")[-1]
        # print(path)
        with open(path+pa+'.jpg','wb') as f:
            f.write(cont)


    for article_url in article_urls:
        # print(article_url)
        response=requests.get(article_url,headers=headers)
        content=response.text
        # print(content)
        pattren = re.compile('(?<=&quot;)(http:\/\/.*?)(?=&quot)', re.S)
        image_urls=re.findall(pattren,content)
        if image_urls:
            for image_url in image_urls:
                saveimg(image_url)
        else:
            pattren = re.compile('(?<=JSON\.parse)(.*?)(?="\),)', re.S)
            urls = re.findall(pattren, content)[0]
            pattren2 = re.compile('(pgc-image)(.*?)(?=\\\\")', re.S)
            urls = urls.replace('\\\\', '')
            urls = re.findall(pattren2, urls)
            urls = list(set(urls))
            # print(urls)
            for url in urls:
                url = url[1]
                image_url = 'http://p3.pstatp.com/origin/pgc-image' + url
                saveimg(image_url)
                # print(image_url)
