import json
import os

import requests
pn=30
# url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&fp=result&queryWord=%E6%96%97%E5%9B%BE%E8%A1%A8%E6%83%85%E5%8C%85&word=%E6%96%97%E5%9B%BE%E8%A1%A8%E6%83%85%E5%8C%85&pn={}&rn=30&1537025889309='.format(pn)
url='https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E7%BE%8E%E5%A5%B3&word=%E7%BE%8E%E5%A5%B3&cg=girl&pn=120&rn=30'
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"
}

if not os.path.exists("./images/"):
    os.makedirs("./images/")
path = "./images/"


for pn in range(2,10):
    pn=(pn-1)*30
    # new_url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&fp=result&queryWord=%E6%96%97%E5%9B%BE%E8%A1%A8%E6%83%85%E5%8C%85&word=%E6%96%97%E5%9B%BE%E8%A1%A8%E6%83%85%E5%8C%85&pn={}&rn=30&1537025889309='.format(pn)
    new_url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E7%BE%8E%E5%A5%B3&word=%E7%BE%8E%E5%A5%B3&cg=girl&pn={}&rn=30'.format(pn)

    print("*************",new_url)
    response = requests.get(new_url, headers=headers, verify=False)

    content = response.text.encode('utf-8')
    # print(content)
    c = json.loads(content, encoding='utf-8')
    # print(c['data'])
    # print(c['data'][0]['thumbURL'])
    for item in c['data']:
        # print(item)
        print('-----------------')
        print(item.get('middleURL'))
        if item.get('middleURL', ''):
            # print(type(item['middleURL']))
            name = item['middleURL'].split('/')[-1]
            # print(name)
            res = requests.get(item['middleURL'])
            con = res.content
            # print(con)
            with open(path + str(name), "wb") as f:
                # 注意写入的内容应该是byte类型
                f.write(con)
        else:
            print('出错了')
