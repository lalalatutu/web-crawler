# --author：lwt--
import json

import requests
from pymongo import MongoClient


def save_to_mongo(data):
    # 创建连接
    client = MongoClient('localhost', 27017)
    # 创建数据库
    db = client.lagou_info
    # 创建集合（表）
    collection = db.lagou
    # 网表中插入数据
    collection.insert_one(data)
city_name=input('请输入城市名字')
kw=input('请输入要搜索的工作')
# 只是爬取了第一页，pn=1，爬取多页可以设置一个变量循环
url = 'https://www.lagou.com/jobs/positionAjax.json'
querystring = {
    "city": city_name,
    "needAddtionalResult": "false"
}
data={
    "first": "true",
    "pn": "1",
    "kd": kw,
}
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '25',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': '_ga=GA1.2.238985228.1535539361; user_trace_token=20180829184241-417fd615-ab78-11e8-b255-5254005c3644; LGUID=20180829184241-417fd8f8-ab78-11e8-b255-5254005c3644; index_location_city=%E5%8C%97%E4%BA%AC; JSESSIONID=ABAAABAAAGFABEF9C0F2AD323E059CECDC51E421502C246; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1537099702,1537422845,1537540512,1537924261; _gid=GA1.2.2085698478.1537924261; LGSID=20180926110320-b9750acc-c138-11e8-a6b5-525400f775ce; TG-TRACK-CODE=index_search; LGRID=20180926110829-717a3730-c139-11e8-bb60-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1537931310; SEARCH_ID=9898aebce13c4ce2aa39800cb62012ad',
    'Host': 'www.lagou.com',
    'Origin': 'https://www.lagou.com',
    'Referer': 'https://www.lagou.com/jobs/list_python?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
    'X-Anit-Forge-Code': '0',
    'X-Anit-Forge-Token': 'None',
    'X-Requested-With': 'XMLHttpRequest',
}
# proxy = {
#     "https": "124.204.64.234:43133"
# }
response = requests.post( url, data=data, headers=headers, params=querystring)
content=response.text
item=json.loads(content,encoding='utf-8')
print(item)
for i in item['content']['positionResult']['result']:
    positionName = i['positionName']
    workYear = i['workYear']
    education = i['education']
    jobNature = i['jobNature']
    createTime = i['createTime']
    city = i['city']
    industryField = i['industryField']
    positionAdvantage = i['positionAdvantage']
    salary = i['salary']
    companySize = i['companySize']
    companyShortName = i['companyShortName']
    financeStage = i['financeStage']
    companyLabelList = i['companyLabelList']
    # print(companyLabelList)
    data = {
        'positionName': positionName,
        'workYear': workYear,
        'education': education,
        'jobNature': jobNature,
        'createTime': createTime,
        'city': city,
        'industryField': industryField,
        'positionAdvantage': positionAdvantage,
        'salary': salary,
        'companySize': companySize,
        'companyShortName': companyShortName,
        'financeStage': financeStage,
        'companyLabelList': companyLabelList,
    }
    save_to_mongo(data)
