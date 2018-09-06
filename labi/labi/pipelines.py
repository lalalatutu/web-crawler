# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

import scrapy
from scrapy.pipelines.images import ImagesPipeline


class LabiPipeline(object):
    def open_spider(self,spider):
        self.file=open('tieba.json','w',encoding='utf-8')

    def close_spider(self,spider):
        self.file.close()

    def process_item(self, item, spider):
        self.file.write(json.dumps(dict(item), ensure_ascii=False) + '\n')
        return item


class MyImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # image_link = item["url"]
        image_link = item["image"]
        yield scrapy.Request(image_link)