# -*- coding: utf-8 -*-
import scrapy
from labi.items import LabiItem


class XiaoxinSpider(scrapy.Spider):
    name = 'xiaoxin'
    allowed_domains = ['tieba.baidu.com']
    offset=0
    kw=input('请输入要爬取的贴吧')
    url = "https://tieba.baidu.com/f?kw="+kw+"&ie=utf-8&pn="
    start_urls=[url+str(offset)]

    def tiezi_url(self,response):
        # print(response.url)
        i=LabiItem()
        i['image']=response.xpath('//div/cc/div/img[@class="BDE_Image"]/@src').extract()[0]
        yield i

    def parse(self, response):
        tiezi_urls=response.xpath('//div[@class="t_con cleafix"]/div/div/div[@class="threadlist_title pull_left j_th_tit "]/a/@href').extract()
        for tiezi in tiezi_urls:
            tiezi="https://tieba.baidu.com"+tiezi
            yield scrapy.Request(tiezi,self.tiezi_url)

        if self.offset<300:
            self.offset+=50
        new_url=self.url+str(self.offset)
        yield scrapy.Request(new_url,callback=self.parse)
