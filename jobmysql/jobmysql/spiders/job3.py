# -*- coding: utf-8 -*-
import scrapy

from jobmysql.items import JobmysqlItem


class Job3Spider(scrapy.Spider):
    name = 'job3'
    allowed_domains = ['51job.com']
    page = 1
    url = "https://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=010000%2C00&keyword=python&curr_page="
    start_urls = [url + str(page)]

    def parse(self, response):
        print("--------------------------------", response.url)
        for url in response.xpath('//div[@class="el"]/p/span/a/@href').extract():
            yield scrapy.Request(url=url, callback=self.real_data)
        next_url = response.xpath('//li[@class="bk"][last()]/a/@href').extract_first()
        print("next_url==", next_url)
        if next_url:
            yield scrapy.Request(url=next_url, callback=self.parse)
        else:
            print("请求结束")

    def real_data(self, response):
        item = JobmysqlItem()
        item['url'] = response.url
        print(item['url'])
        item['title'] = response.xpath('//h1/@title').extract_first()
        # print(type(item['title']))
        item['location'] = response.xpath('//div[@class="cn"]/p[2]/text()[1]').extract_first().strip()
        # print(type(item['location']))
        item['company_name'] = response.xpath('//div[@class="cn"]/p/a[1]/text()').extract_first().strip()
        # print(type(item['company_name']))
        item['salary'] = response.xpath('//div[@class="cn"]/strong/text()').extract_first()
        # print(type(item['salary']))
        item['company_info'] = response.xpath('//div[@class="com_tag"]/p/text()').extract()
        item['company_info']=''.join(item['company_info'])
        # print(type(item['company_info']))
        item['experience'] = response.xpath('//div[@class="cn"]/p[2]/text()[2]').extract_first().strip()
        job_info = response.xpath(
            '//div[@class="bmsg job_msg inbox"]/p/text()|//div[@class="bmsg job_msg inbox"]/text()').extract()
        item['job_info'] = "".join(job_info).strip()
        address = response.xpath('//div[@class="bmsg inbox"]/p[@class="fp"]/text()').extract()
        item['address'] = "".join(address).replace('\r', '').replace('\n', '').replace('\t', '')
        # print(item['location'])
        yield item
