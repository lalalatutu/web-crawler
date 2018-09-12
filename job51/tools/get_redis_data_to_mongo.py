import pymongo
import pymysql
import redis
import json

# mongodb的客户端
client=pymongo.MongoClient(host='127.0.0.1',port=27017)
# redis的客户端
redis_client=redis.StrictRedis(host='192.168.11.68',port=6379,db=0)

sina=client['job']

sina_item=sina['job']
while True:
    source,data=redis_client.blpop(['job:items'])
    print('source===',source)
    print('data===', data)
    data=data.decode('utf-8')
    data=json.loads(data)
    sina_item.insert_one(data)