# -*- coding: utf-8 -*-
import os
import scrapy
from Sina.items import SinaItem


class SinaGuideSpider(scrapy.Spider):
    name = 'sina_guide'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    def detail_tiezi(self,response):
        item=response.meta['item']
        # print('---------')
        # print(item)
        # print(response.url)
        item['tiezi_url']=response.url
        tiezi_title=response.xpath('//h1/text()|//h2[@id="artibodyTitle"]/text()').extract_first()
        tiezi_content=response.xpath('//div[@class="article"]//p/text()|//div[@id="artibody"]//p/text()').extract()
        if tiezi_content:
            tiezi_content="".join(tiezi_content)
        # print(tiezi_title)
        item['tiezi_title']=tiezi_title
        item['tiezi_content']=tiezi_content
        yield item

    def seconde_detail(self,response):
        item=response.meta['item']
        urls=response.xpath('//a/@href').extract()
        parent_url=item['parent_url']
        # 当前页所有的链接
        for url in urls:
            if url.startswith(parent_url) and url.endswith(".shtml"):
                yield scrapy.Request(url,callback=self.detail_tiezi,meta={'item':item})


    def parse(self, response):
        print(response.url)
        parent_titles = response.xpath('//div[@id="tab01"]//h3[@class="tit02"]/a/text()').extract()
        parent_urls = response.xpath('//div[@id="tab01"]//h3[@class="tit02"]/a/@href').extract()
        sub_titles = response.xpath('//div[@id="tab01"]//ul[@class="list01"]/li/a/text()').extract()
        sub_urls = response.xpath('//div[@id="tab01"]//ul[@class="list01"]/li/a/@href').extract()
        # 大标题
        for index in range(len(parent_titles)):
            parent_title = parent_titles[index]
            parent_url = parent_urls[index]
            # print(parent_url,parent_title)

            # 大标题下循环取小标题
            for index_sub in range(len(sub_titles)):
                sub_title = sub_titles[index_sub]
                sub_url = sub_urls[index_sub]
                if sub_url.startswith(parent_url):
                    tiezi_path = "./datas/" + parent_title + "/" + sub_title
                    if not os.path.exists(tiezi_path):
                        os.makedirs(tiezi_path)
                # print(sub_url,sub_title)
                    item = SinaItem()
                    item['parent_title']=parent_title
                    item['parent_url'] = parent_url
                    item['sub_title'] = sub_title
                    item['sub_url'] = sub_url
                    item['tiezi_path'] = tiezi_path
                    yield scrapy.Request(sub_url,callback=self.seconde_detail,meta={'item':item})
