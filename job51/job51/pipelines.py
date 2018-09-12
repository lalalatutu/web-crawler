# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime


class ExamplePipeline(object):

    #第三个参数是：爬虫MyCrawler类的实例
    def process_item(self, item, spider):
        #添加爬取时间
        item["crawled"] = datetime.utcnow()
        #添加爬虫的名称：myspider_redis+"windows_afu"
        item["spider"] = spider.name+"__windows_llllllwt"
        return item


class Job51Pipeline(object):
    def process_item(self, item, spider):
        return item
