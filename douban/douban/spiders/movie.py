# -*- coding: utf-8 -*-
import scrapy

from douban.items import DoubanItem


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['movie.douban.com']
    offset = 0
    start_urls = ["https://movie.douban.com/top250?start=" + str(offset)]

    def parse(self, response):
        print(response.url)
        for node in response.xpath('//div[@class="item"]'):
            item = DoubanItem()
            item['name'] = node.xpath('./div/div/a/span[1]/text()').extract()[0]
            item['image'] = node.xpath('./div/a/img/@src').extract()[0]
            item['star'] = node.xpath('./div/div/div/span[2]/text()').extract()
            info = node.xpath('.//div[@class="bd"]/p[1]/text()').extract()
            if info:
                info = "".join(info)
            item['info'] = info
            desc = node.xpath('//span[@class="inq"]/text()').extract()
            if desc:
                desc = desc[0]
            item['desc'] = desc
            # print("-------------------------------------------")
            # print(item)
            yield item
            if self.offset < 225:
                self.offset += 25
            next_page_url = "https://movie.douban.com/top250?start=" + str(self.offset)
            yield scrapy.Request(next_page_url, callback=self.parse)
