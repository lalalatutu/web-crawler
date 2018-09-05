一、Spider爬虫参数介绍

二、CrawlSpider（规则爬虫）
1.创建spider爬虫：scrapy genspider tencentPosition
2.创建CrawlSpider爬虫：scrapy genspider -t crawl tencentPosition2 hr.tencent.com

检查或者修改允许的域名
检查修改起始路径


3.快速使用规则爬虫，爬取所有的招聘信息
4.讲解细节
创建CrawlSpider爬虫：scrapy genspider -t crawl tencentPosition3 hr.tencent.com



三、CrawlSpider爬虫项目--爬虫政府投诉平台信息

1.、CrawlSpider爬虫项目--爬虫政府投诉平台信息

1.1 爬取目标
帖子的标题：title
投诉编号：number
帖子的链接：url
帖子的内容：content

1.2 分析网站的结构

第一步得到帖子的链接
规则里面的正则写法：question/\d+/\d+\.shtml (原始question/201809/384498.shtml)

第二步请求帖子--规则爬虫默认帮我请求了

第三步请求下一页
规则里面的正则写法：type=\d+&page=\d+  （原始type=4&page=150）


1.3 代码实现流程

1.3.1 创建项目命令：scrapy startproject Dounguan

      进入项目：cd Dounguan 
      创建规则爬虫命令：scrapy genspider -t crawl dongguan_crawl wz.sun0769.com

      运行爬虫的命令：scrapy crawl dongguan_crawl


1.3.2 得到当前页的所有帖子的链接，并且请求后得到数据封装在Respons对象回调parse_item


1.3.3 爬取目标对应的xpath

帖子标题和编号的xpath:  //div[@class="pagecenter p3"]//strong[@class="tgray14"]/text()
帖子的标题：title
投诉编号：number
帖子的链接：url



帖子的内容：content
//div[@class="pagecenter p3"]//div[@class="content text14_2"]/div[@class="c1 text14_2"]/text()

帖子内容有图的：//div[@class="pagecenter p3"]//div[@class="contentext"]/text()


1.3.4 代码实现


import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Dounguan.items import DounguanItem

#规则爬虫DongguanCrawlSpider，继承的父类是CrawlSpider
class DongguanCrawlSpider(CrawlSpider):
    #爬虫的名称
    name = 'dongguan_crawl'
    #允许爬取的范围
    allowed_domains = ['wz.sun0769.com']
    #起始路径
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=30']

    rules = (
        #follow=False先爬取当前页
        #得到当前页的所有帖子的链接，并且请求后得到数据封装在Respons对象回调parse_item
        Rule(LinkExtractor(allow=r'question/\d+/\d+\.shtml'), callback='parse_item', follow=False),
    )


    def parse_item(self, response):
        print("---------------------------------------------")
        #一个帖子的内容
        print("response.url==",response.url)
        #帖子链接
        url = response.url
        #提问：长期饱受油烟污染  编号:195558
        title_number = response.xpath('//div[@class="pagecenter p3"]//strong[@class="tgray14"]/text()').extract()[0]
        #--->['提问：长期饱受油烟污染','编号:195558','']
        title_number = title_number.split("  ")
        #帖子的标题
        #---->提问：长期饱受油烟污染-->['提问','长期饱受油烟污染']
        title = title_number[0].split("：")[1]

        #帖子的编号
        #'编号:195558' --> ["编号","195558"]
        number =  title_number[1].split(":")[1]

        #帖子的内容
        content = response.xpath('//div[@class="pagecenter p3"]//div[@class="content text14_2"]/div[@class="c1 text14_2"]/text()|//div[@class="pagecenter p3"]//div[@class="contentext"]/text()').extract()[0]

        item = DounguanItem()
        item["url"] = url
        item["title"] = title
        item["number"] = number
        item["content"] = content

        print(item)

        yield item



 在管道文件保存数据

import json

class DounguanPipeline(object):
    def open_spider(self,spider):
        #当爬虫开始的时候执行
        self.file = open("东莞阳光项目.json","w",encoding="utf-8")
        print("当爬虫开始的时候执行-------------------------------------")

    def close_spider(self,spider):
        self.file.close()
        print("当爬虫结束的时候执行-------------------------------------")
    def process_item(self, item, spider):
        #传入一条一条的数据
        self.file.write(json.dumps(dict(item),ensure_ascii=False) +"\n")
        return item







2、Spider爬虫项目----爬虫政府投诉平台信息

1.分析网站的结构

2.实现得到所有的页的链接

3.请求每页，再去解析帖子链接


4.创建Spider爬虫命令：scrapy genspider dongguan_spider wz.sun0769.com

5.代码实现

得到帖子的链接的xpath :  //a[@class="news14"]/@href





扩展设置查看代理服务器

views.py

class UserAgentProxyServerView(APIView):

	def get(self, request):
		data = {}
		data['remote_addr(请求的ip)'] = request.META.get('REMOTE_ADDR')
		data['User-agent(请求头)'] = request.META.get('HTTP_USER_AGENT')
		data['Referer(跳转处)'] = request.META.get('HTTP_REFERER')
		data['Cookie(令牌)'] = request.META.get('HTTP_COOKIE')
		data['Method(请求方法)'] = request.method
		json_content = json.dumps(data, ensure_ascii=False)
		return HttpResponse(json_content, content_type='application/json', charset='utf-8')



urls.py下

url(r"^test/",UserAgentProxyServerView.as_view(),name="test")


把代码上传到阿里云服务器

请求地址：

http://118.190.202.67:8000/test/



四、Request/Response

五、三种scrapy模拟登陆策略

六、使用案例-爬取豆瓣电影排名前250部电影
