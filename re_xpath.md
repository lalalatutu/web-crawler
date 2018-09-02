# 提取结构化与非结构化数据--正则、xpath
## 一.1 Re模块直接使用的一些常用方法主要有：
  match 方法：从起始位置开始查找，一次匹配
  search 方法：从起始位置开始查找，一次匹配
  findall 方法：全部匹配，返回列表
  finditer 方法：全部匹配，返回迭代器
  split 方法：分割字符串，返回列表
  sub 方法：替换
  忽略大小写（re.I）和得到匹配的位置
  2 使用compile 函数后的方法
    [kəmˈpaɪl] 
    1）使用 compile() 函数将正则表达式的字符串形式编译为一个 Pattern 对象

    2）通过 Pattern 对象提供的一系列方法对文本进行匹配查找，获得匹配结果，一个 Match 对象。

    3）最后使用 Match 对象提供的属性和方法获得信息，根据需要进行其他的操作
  3 compile 函数用于编译正则表达式，生成一个 Pattern 对象，
    match 方法：从起始位置开始查找，也可以设置从某个位置开始匹配，一次匹配
    search 方法：从任何位置开始查找，也可以设置从某个位置开始匹配，一次匹配
    findall 方法：全部匹配，也可以设置从某个位置开始匹配，返回列表
    finditer 方法：全部匹配，也可以设置从某个位置开始匹配，返回迭代器
    split 方法：分割字符串，返回列表
    sub 方法：替换，替换多少个字符串。
# xpath 常用，很好用
 一.1.Chrome插件 XPath Helper(必须要安装)
    2.Xpath测试工具的使用(最好安装)
    . 安装插件 XPath Helper和Xpath测试工具使用
https://my.oschina.net/u/3892643/blog/1840014

 # 案例--使用代码运行XPath实例测试
3.1 获取所有的 <li> 标签
from lxml import etree

html = etree.parse('./hello.html')
显示etree.parse() 返回类型

print(type(html)  )
result = html.xpath('//li')
print(result)  # 打印<li>标签的元素集合
print(len(result))
print(type(result))
print(type(result[0]))
3.2. 继续获取<li> 标签的所有 class属性
from lxml import etree

html = etree.parse('./hello.html')
显示etree.parse() 返回类型

result = html.xpath('//li/@class')
print(result)  # 打
3.3. 继续获取<li>标签下hre f为 link1.html 的 <a>标签
from lxml import etree

html = etree.parse('./hello.html')
 显示etree.parse() 返回类型
result = html.xpath('//li/a[@href="link1.html"]')
print(result)  # 打印<li>标签的
运行结果

3.4. 获取<li> 标签下的所有 <span> 标签
from lxml import etree

html = etree.parse('./hello.html')
显示etree.parse() 返回类型
result = html.xpath('//li/span')#注意这么写是不对的：
因为 / 是用来获取子元素的，而 <span> 并不是 <li> 的子元素，所以，要用双斜杠
result = html.xpath('//li//span')
print(result)  # 打印<li
运行结果

3.5. 获取 <li> 标签下的<a>标签里的所有 class

from lxml import etree

html = etree.parse("./hello.html")
li_lists = html.xpath("//li/a//@class")
print(li_lists)
3.6. 获取最后一个 <li> 的 <a> 的 href
from lxml import etree
#需求:获取最后一个 <li> 的 <a> 的 href
html = etree.parse("./hello.html")
# 谓语 [last()] 可以找到最后一个元素
li_lists = html.xpath('//li[last()]/a/@href')
print(li_lists)
  
from lxml import etree
#需求:获取倒数第二个元素li的内容,也就是fourth item
html = etree.parse("./hello.html")
li_lists = html.xpath('//li[last()-1]/a/text()')
print(li_lists)

第二种方式
from lxml import etree
#需求:获取倒数第二个元素li的内容,也就是fourth item
html = etree.parse("./hello.html")
#返回a标签对象
li_lists = html.xpath('//li[last()-1]/a')
#从a标签对象中取出text
print(li_lists[0].text)

3.8. 获取 class 值为 bold 的标签名
from lxml import etree
#需求:8.获取 class 值为 bold 的标签名
html = etree.parse("./hello.html")
li_lists = html.xpath('//*[@class="bold"]')
print(li_lists)
print(li_lists[0].tag)
print(li_lists[0].text)

3.9. 注意//li/@class和//*/@class不一样
//li/@class意思是所有li标签内的名字叫class的属性
