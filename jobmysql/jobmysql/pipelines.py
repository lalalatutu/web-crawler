# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class JobmysqlPipeline(object):
    def process_item(self, item, spider):
        client=pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='atguigu',
            db='scrapy',
            port=3306,
            charset='utf8'
        )
        cursor=client.cursor()
        print("mysql connect succes")
        try:
            params = [item['url'], item['title'], item['location'], item['company_name'], item['salary'],item['company_info'], item['experience'], item['job_info'], item['address']]
            # 注意写入的内容的类型需要是字符串
            sql = "INSERT INTO job (url, title,location,company_name,salary,company_info,experience,job_info ,address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s )"
            cursor.execute(sql,params)
            client.commit()
        except Exception as e:
            print("出错了==", e)
        return item

