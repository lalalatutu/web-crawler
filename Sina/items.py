# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    parent_title = scrapy.Field()
    parent_url = scrapy.Field()
    sub_title = scrapy.Field()
    sub_url = scrapy.Field()
    tiezi_url = scrapy.Field()
    tiezi_path = scrapy.Field()
    tiezi_title = scrapy.Field()
    tiezi_content = scrapy.Field()
