
import pymysql
import redis
import time
import json
# 得到redis的数据  然后存入mysql

# mysql的客户端
client = pymysql.connect(host="127.0.0.1", user="root", password="atguigu",
                         db="scrapy", port=3306, charset='utf8')

cursor = client.cursor()

# redis的客户端
reids_client = redis.StrictRedis(host='192.168.11.68', port=6379, db=0)

while True:
    try:
        source, data = reids_client.blpop(["sina_guide:items"])
        print("--------------------")
        # time.sleep(1)
        print("source==", source)
        data = data.decode("utf-8")
        print("data==", data)
        print("data==", type(data))
        item = json.loads(data)

        params = [item['parent_title'], item['sub_title'], item['sub_url'], item['tiezi_path'], item['tiezi_url'],
                  item['tiezi_title'],  item['crawled'],item['spider']]
        # 注意插入的字段要和数据库中表的字段相同
        sql = "INSERT INTO sina2(parent_title, sub_title,sub_url,tiezi_path,tiezi_url,tiezi_title,crawled,spider) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s )"
        # 执行sql语句
        cursor.execute(sql, params)

        # 提交事务
        client.commit()
    # 字典
    except Exception as e:
        print("出错了==", e)
