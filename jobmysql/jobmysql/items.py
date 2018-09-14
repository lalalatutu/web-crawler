# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobmysqlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    location = scrapy.Field()
    company_name = scrapy.Field()
    salary = scrapy.Field()
    company_info = scrapy.Field()
    experience = scrapy.Field()
    job_info = scrapy.Field()
    address = scrapy.Field()
    id=scrapy.Field()