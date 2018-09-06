# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from labi.items import LabiItem


class Xiaoxin2Spider(CrawlSpider):
    name = 'xiaoxin2'
    allowed_domains = ['tieba.baidu.com']
    kw = input('请输入要爬取的贴吧')
    url = "https://tieba.baidu.com/f?kw=" + kw + "&ie=utf-8&pn=0"
    start_urls = [url]

    rules = (
        Rule(LinkExtractor(allow=r'/p/\d+'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'&pn=\d+'),follow=True),
        Rule(LinkExtractor(allow=r'^https://imgsa\.baidu\.com'),follow=True)
    )

    def parse_item(self, response):
        i = LabiItem()
        i['url'] = response.url
        i['image']=response.xpath('//div/cc/div/img[@class="BDE_Image"]/@src').extract()[0]
        
        yield i