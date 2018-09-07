# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class SinaTextSavePipeline(object):
    def process_item(self, item, spider):
        tiezi_content = item['tiezi_content']
        tiezi_url = item['tiezi_url']
        tiezi_path = item['tiezi_path']
        file_name = tiezi_url[7:tiezi_url.rfind(".")].replace("/", "_").replace(".","_") + ".txt"
        with open(tiezi_path + "/" + file_name, "w", encoding="utf-8") as f:
            f.write(tiezi_content)
        return item


class SinaPipeline(object):
    def open_spider(self, spider):
        self.file = open('sina.json', 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        self.file.write(json.dumps(dict(item), ensure_ascii=False) + '\n')
        return item
