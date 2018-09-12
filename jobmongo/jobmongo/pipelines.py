# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymongo
from jobmongo.settings import MONGO_HOST,MONGO_PORT, MONGO_DBNAME, MONGO_SHEETNAME


class JobmongoPipeline(object):
    def open_spider(self,spider):
        self.file=open('job.json','w',encoding='utf-8')
        host = MONGO_HOST
        port = MONGO_PORT
        db_name = MONGO_DBNAME
        sheet_name = MONGO_SHEETNAME
        client=pymongo.MongoClient(host=host,port=port)
        job=client[db_name]
        self.sheetname=job[sheet_name]

    def close_spider(self,spider):
        self.file.close()

    def process_item(self, item, spider):
        dict_item = dict(item)
        self.file.write(json.dumps(dict_item, ensure_ascii=False) + "\n")
        # 插入数据
        self.sheetname.insert_one(dict_item)
        return item
