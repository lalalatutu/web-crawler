import json

import requests
from pymongo import MongoClient
kw=input('请输入要搜索的关键词')
city=input('请输入要爬取的城市的拼音，例如beijing:')
url='https://fe-api.zhaopin.com/c/i/sou?pageSize=60&cityId={}&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw={}&kt=3&lastUrlQuery=%7B'.format(city,kw)
print(url)
response = requests.get(url)
content = response.text
# print(content)
# with open('zhilian.html','w',encoding='utf-8')as f:
#     f.write(content)

def save_to_mongo(data):
    # 创建连接
    client = MongoClient('localhost', 27017)
    # 创建数据库
    db = client.zhaopin_info
    # 创建集合（表）
    collection = db.zhaopin
    # 网表中插入数据
    collection.insert_one(data)


# with open('zhilian.html','r',encoding='utf-8')as f:
#     content=f.read()
# print(content)
item=json.loads(content,encoding='utf-8')
for i in item['data']['results']:
    # print(i)
    jobName=i['jobName']
    salary=i['salary']
    workingExp=i['workingExp']['name']
    eduLevel=i['eduLevel']['name']
    company=i['company']['name']
    company_size=i['company']['size']['name']
    company_type=i['company']['type']['name']
    welfare=i.get('welfare')
    city_name=i['city']['display']
    item = {
        'jobName': jobName,
        'salary': salary,
        'workingExp': workingExp,
        'eduLevel': eduLevel,
        'company': company,
        'company_size': company_size,
        'company_type': company_type,
        'welfare': welfare,
        'city_name': city_name,
    }
    save_to_mongo(item)