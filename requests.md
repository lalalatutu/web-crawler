## Requests: 让 HTTP 服务更加简洁
虽然Python的标准库中 urllib2(urllib.request在python3中) 模块已经包含了平常我们使用的大多数功能，但是它的 API 使用起来让人感觉不太好，而 Requests 自称 “HTTP for Humans”，说明使用更简洁方便。
Requests 唯一的一个非转基因的 Python HTTP 库，人类可以安全享用：
Requests 继承了urllib2的所有特性。Requests支持HTTP连接保持和连接池，支持使用cookie保持会话，支持文件上传，支持自动确定响应内容的编码，支持国际化的 URL 和 POST 数据自动编码。
requests 的底层实现其实就是 urllib3
Requests的文档非常完备，中文文档也相当不错。Requests能完全满足当前网络的需求，支持Python 2.6–2.7 & 3.3–3.7，而且能在PyPy下完美运行。
开源地址：https://github.com/kennethreitz/requests
中文文档 API： http://docs.python-requests.org/zh_CN/latest/index.html
2. 基本GET请求（headers参数 和 parmas参数）
2.1  最基本的GET请求可以直接用get方法
import requests
response = requests.get("http://www.baidu.com/")
# 也可以这么写
# response = requests.request("get", "http://www.baidu.com/")
#post请求
# response = requests.post("http://www.baidu.com/")

#打印是什么请求
print(response.request)
#打印服务器返回的内容
print(response.content)
2.2  添加 headers 和 查询参数
3. User-Agent--代表不同浏览器的身份
3.1 User-Agent 是反爬虫的第一步

但是这样直接用Requests给一个网站发送请求的话，确实略有些唐突了，就好比，人家每家都有门，你以一个路人的身份直接闯进去显然不是很礼貌。而且有一些站点不喜欢被程序（非人为访问）访问，有可能会拒绝你的访问请求。
但是如果我们用一个合法的身份去请求别人网站，显然人家就是欢迎的，所以我们就应该给我们的这个代码加上一个身份，就是所谓的User-Agent头。

浏览器 就是互联网世界上公认被允许的身份，如果我们希望我们的爬虫程序更像一个真实用户，那我们第一步，就是需要伪装成一个被公认的浏览器。用不同的浏览器在发送请求的时候，会有不同的User-Agent头。 Requests默认的User-Agent头为：python-requests/2.18.4
3.2 案例--代表不同浏览器的身份

如果想添加 headers，可以传入headers参数来增加请求头中的headers信息。如果要将参数放在url中传递，可以利用 params （参数自动帮我们汉字urlencode编码）。
import requests
kw = {'wd':'尚硅谷'}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
# params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
response = requests.get("http://www.baidu.com/s?", params = kw, headers = headers)
# 查看响应内容，response.text 返回的是Unicode格式的数据
print(response.text)
# 查看响应内容，response.content返回的字节流数据
print(response.content)
# 查看完整url地址
print(response.url)
# 查看响应头部字符编码
print(response.encoding)
# 查看响应码
print(response.status_code)
运行结果

使用response.text 时，Requests 会基于 HTTP 响应的文本编码自动解码响应内容，大多数 Unicode 字符集都能被无缝地解码。

使用response.content 时，返回的是服务器响应数据的原始二进制字节流，可以用来保存图片等二进制文件。

没有网络的时候也会报错，肯定的，你懂的。


4. 基本POST请求（data参数）
4.1. 最基本的GET请求可以直接用post方法
但是这个请求仍然是post请求，只是用post请求可以得到get可以请求的链接的数据
import requests
response = requests.post("http://www.baidu.com/")
4.2. 案例--post请求案例
对于 POST 请求来说，我们一般需要为它增加一些参数。那么最基本的传参方法可以利用 data 这个参数。
请求http://httpbin.org/post的连接

import requests

url = "http://httpbin.org/post"
# url = "http://127.0.0.1:8080"
# 组装表单数据
formdata ={"name":"zhangsan","age":"18"}
#请求头
headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

#post请求
response = requests.post(url, data=formdata, headers=headers)

print(response.text)
#返回url
print(response.url)
# 如果是json文件可以直接显示
print(response.json())
运行结果：

5. 获取AJAX加载的内容
Ajax 即“Asynchronous Javascript And XML”（异步 JavaScript 和 XML），是指一种创建交互式网页应用的网页开发技术。
Ajax = 异步 JavaScript 和 XML（标准通用标记语言的子集）。
Ajax 是一种用于创建快速动态网页的技术。
Ajax 是一种在无需重新加载整个网页的情况下，能够更新部分网页的技术。
通过在后台与服务器进行少量数据交换，Ajax 可以使网页实现异步更新。这意味着可以在不重新加载整个网页的情况下，对网页的某部分进行更新。

有些网页内容使用AJAX加载，只要记得，AJAX一般返回的是JSON,直接对AJAX地址进行post或get，就返回JSON数据了。
"作为一名爬虫工程师，你最需要关注的，是数据的来源"
例如网站：豆瓣电影
https://movie.douban.com/

就是ajax效果



5.1 找到ajax里面有http的get请求



5.2 这是内部真正请求的地址
https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20

import requests
url = "https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=10"
#使用get请求得到数据
response = requests.get(url)
#打印返回的数据
print(response.text)

执行效果：


5.3 GET和POST请求的区别

1)GET方式是直接以链接形式访问，链接中包含了所有的参数，服务器端用Request.QueryString获取变量的值。如果包含了密码的话是一种不安全的选择，不过你可以直观地看到自己提交了什么内容。

2)POST则不会在网址上显示所有的参数，服务器端用Request.Form获取提交的数据，在Form提交的时候。但是HTML代码里如果不指定 method 属性，则默认为GET请求，Form中提交的数据将会附加在url之后，以?分开与url分开。

3)表单数据可以作为 URL 字段（method="get"）或者 HTTP POST （method="post"）的方式来发送。比如在下面的HTML代码中，表单数据将因为 （method="get"） 而附加到 URL 上：
<form action="form_action.asp" method="get">
<p>First name: <input type="text" name="fname" /></p>
<p>Last name: <input type="text" name="lname" /></p>
<input type="submit" value="Submit" /></form>


6. 代理（proxies参数）
1私密代理验证（特定格式） 和 Web客户端验证（auth 参数）
2. ProxyHandler处理器（代理设置）
2.1 代理的原理

使用代理IP，这是爬虫/反爬虫的第二大招，通常也是最好用的。
很多网站会检测某一段时间某个IP的访问次数(通过流量统计，系统日志等)，如果访问次数多的不像正常人，它会禁止这个IP的访问。
所以我们可以设置一些代理服务器，每隔一段时间换一个代理，就算IP被禁止，依然可以换个IP继续爬取。
requests中通过proxies来设置使用代理服务器
免费的开放代理获取基本没有成本，我们可以在一些代理网站上收集这些免费代理，测试后如果可以用，就把它收集起来用在爬虫上面。
免费短期代理网站举例：
西刺免费代理IP：http://www.xicidaili.com/
快代理免费代理：https://www.kuaidaili.com/free/inha/
全网代理IP：http://http.zhiliandaili.com/
测试代理服务器是否可行：https://www.kuaidaili.com/check


2.2 案例--免费代理和随机代理
要多用几个，有些是失效的
西刺免费代理IP：http://www.xicidaili.com/

代码
import  requests
# 根据协议类型，选择不同的代理
proxies = {
 "https":"183.129.207.73:14823",
# "https":"https://183.129.207.73:14823",#这种也可以
 "http": "118.190.95.43:9001",
# "http": "http://118.190.95.43:9001",#也可以

}
# response = requests.get("http://118.190.202.67:8000/", proxies=proxies)
response = requests.get("http://www.baidu.com/", proxies=proxies)
print(response.content.decode("utf-8"))

这些免费开放代理一般会有很多人都在使用，而且代理有寿命短，速度慢，匿名度不高，HTTP/HTTPS支持不稳定等缺点（免费没好货）。
所以，专业爬虫工程师或爬虫公司会使用高品质的私密代理，这些代理通常需要找专门的代理供应商购买，再通过用户名/密码授权使用（舍不得孩子套不到狼）。

2.3 案例--独享代理
快代理免费代理：https://www.kuaidaili.com/free/inha/
注册后就可以购买，实验的话买便宜的独享代理即可
登录快速免费代理网站账号和密码：
账号：trygf521@126.com
密码：afu123456

国内高匿代理IP，只能看待代理服务器的ip,如果封ip那么只封代理服务器的IP;
 国内透明代理IP:不光看待代理服务器的ip，还可以看到发送请求电脑的ip私密代理
若你的代理需要使用HTTP Basic Auth，可以使用 http://user:password@host/ 语法：
proxies = {
"http": "http://user:pass@10.10.1.10:3128/",
}


import requests
# 如果代理需要使用HTTP Basic Auth，可以使用下面这种格式：
proxy = { "http":"http://trygf521:a4c4avg9@114.67.228.126:16818/" }
response = requests.get("http://www.baidu.com", proxies = proxy)
print(response.text)

运行结果：

实验了，请求https://www.baidu.com也可以


通过环境变量 HTTP_PROXY 和 HTTPS_PROXY 来配置代理。
$ export HTTP_PROXY="http://12.34.56.79:9527"
$ export HTTPS_PROXY="http://12.34.56.79:9527"

$ python
>>> import requests
>>> requests.get("http://example.org")
若你的代理需要使用HTTP Basic Auth，可以使用 http://user:password@host/ 语法：
proxies = {
    "http": "http://user:pass@10.10.1.10:3128/",}
要为某个特定的连接方式或者主机设置代理，使用 scheme://hostname 作为 key， 它会针对指定的主机和连接方式进行匹配。
proxies = {'http://10.20.1.128': 'http://10.10.1.10:5323'}
注意，代理 URL 必须包含连接方式。

7. Cookies和Sission
1 Cookies
如果一个响应中包含了cookie，那么我们可以利用 cookies参数拿到：
import requests
response = requests.get("http://www.baidu.com/")
# 7. 返回CookieJar对象:
cookiejar = response.cookies
# 8. 将CookieJar转为字典：
cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
print(cookiejar)
print(cookiedict)
运行结果：

2 案例--使用Session实现人人网登录
在 requests 里，session对象是一个非常常用的对象，这个对象代表一次用户会话：从客户端浏览器连接服务器开始，到客户端浏览器与服务器断开。
会话能让我们在跨请求时候保持某些参数，比如在同一个 Session 实例发出的所有请求之间保持 cookie 。   

import requests
# 1. 创建session对象，可以保存Cookie值
ssion = requests.session()
# 2. 处理 headers
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
# 3. 需要登录的用户名和密码
data = {"email":"yangguangfu2017@163.com", "password":"afu123456"}
# 4. 发送附带用户名和密码的请求，并获取登录后的Cookie值，保存在ssion里
ssion.post("http://www.renren.com/PLogin.do", data = data)
# 5. ssion包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页面
response = ssion.get("http://www.renren.com/880792860/profile")
# 6. 打印响应内容
print(response.text)
运行结果：

3. 案例--使用Cookie登录京东商城

    京东测试账号：
账号：python_afu
密码：afu123456






Request headers
':authority':'home.jd.com',
':method':'GET',
':scheme':'https',
'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'accept-encoding':'gzip, deflate, br',
'accept-language':'zh-CN,zh;q=0.9,en;q=0.8',
'cache-control':'max-age=0',
'cookie':'iddsss',

注意如果有冒号，要去掉哦，复制到cookie信息需要加引号，使用正则匹配，正则分组


下面的代码使用到了Cookie,因为Cookie是有期限的，所有需要重新抓包找到Cookie,直接运行会报错
#coding=utf-8
# 获取一个有登录信息的Cookie模拟登陆
import requests
# 1. 构建一个已经登录过的用户的headers信息
headers = {
'authority':'home.jd.com',
'method':'GET',
'scheme':'https',
'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'accept-encoding':'gzip, deflate, br',
'accept-language':'zh-CN,zh;q=0.9,en;q=0.8',
'cache-control':'max-age=0',
'cookie':'ipLoc-djd=1-72-2799-0; shshshfpb=05305bbfd662293965660cbd39b2b4b80aeb9ab22ad43f6815b5ff7ffa; shshshfpa=ed1b53d0-8e70-3a3b-57e0-687045756170-1533028289; __jda=122270672.1535304790021629950410.1535304790.1535304790.1535304790.1; __jdc=122270672; __jdv=122270672|direct|-|none|-|1535304790021; __jdu=1535304790021629950410; wlfstk_smdl=fvn1f4pfetdqrvci1w8t51vwy86heqau; TrackID=1Sl3wiuNGyUHmjSPnTn6RFEya_FTuPI5w6IL7LX-DyPAhVQ3qSiCrnqNlsL6ruJif59-w6Uga9WgbOuVgBK1Hew; thor=AE86F17153107F9744F5268A88E4731C45C7B857C2D8B269992EBE6692E23E9291C85ED861C7C5AFB77C7B162D32C8C38D69C351EFD04EAE3D44C3A23041A41F53044C1B2EB15D9257BF58AFC98955DFCF58C03BA32643AFA645A58BDCC21EF255647E56045239BC8F64989FDB29BC626ADEE5959E868E0148B8731C94C418FB6023EAA7A57BC49C6FBEE2752C2024DB; pinId=tF0w3lsgbrKuuR-PW68-4Q; pin=python_afu; unick=python_afu; ceshi3.com=000; _tp=wmA28pFNyQS3czxsK1OIHA%3D%3D; _pst=python_afu; __jdb=122270672.3.1535304790021629950410|1.1535304790; 3AB9D23F7A4B3C9B=3JRK7JWTXAB65RWQ7VTATRTEE5FP3SSEWYN22GGU2VEDZ3SITYGMP53UFOY3XV7YVH7SF7PSJOLRKIYIWDCK6HD2N4',
'upgrade-insecure-requests':'1',
'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',

}
# 2. 通过headers里的报头信息（主要是Cookie信息），构建Request对象
# 3. 直接访问renren主页，服务器会根据headers报头信息（主要是Cookie信息），判断这是一个已经登录的用户，并返回相应的页面
response =  requests.get("https://home.jd.com/",headers=headers)
# 4. 打印响应内容
print(response.text)

运行效果：

Cookies在爬虫方面最典型的应用是判定注册用户是否已经登录网站，用户可能会得到提示，是否在下一次进入此网站时保留用户信息以便简化登录手续

8. 处理HTTPS请求 SSL证书验证
https://www.12306.cn/mormhweb/
1 https和SSL之间是什么关系
https和SSL之间是什么关系：https就是在http上面加了一层ssl协议，在http站点上部署SSL数字证书就变成了https。

现在随处可见 https 开头的网站，requests可以为 HTTPS 请求验证SSL证书，就像web浏览器一样，如果网站的SSL证书是经过CA认证的，则能够正常访问，如：https://www.baidu.com/等。
如果SSL证书验证不通过，或者操作系统不信任服务器的安全证书，比如浏览器在访问12306网站如：https://www.12306.cn/mormhweb/的时候，会警告用户证书不受信任。（12306 网站证书是自己做的，没有通过CA认证）

扩展阅读：
电子商务认证授权机构（CA, Certificate Authority），也称为电子商务认证中心，是负责发放和管理数字证书的权威机构，并作为电子商务交易中受信任的第三方，承担公钥体系中公钥的合法性检验的责任。例如北京的数字认证中心：http://www.bjca.org.cn/

2 关于CA认证（数字证书认证中心）
CA(Certificate Authority)是数字证书认证中心的简称，是指发放、管理、废除数字证书的受信任的第三方机构，如
北京数字认证股份有限公司：http://www.bjca.org.cn/、
上海市数字证书认证中心有限公司：http://www.sheca.com/
等...
CA的作用是检查证书持有者身份的合法性，并签发证书，以防证书被伪造或篡改，以及对证书和密钥进行管理。
现实生活中可以用身份证来证明身份， 那么在网络世界里，数字证书就是身份证。和现实生活不同的是，并不是每个上网的用户都有数字证书的，往往只有当一个人需要证明自己的身份的时候才需要用到数字证书。
普通用户一般是不需要，因为网站并不关心是谁访问了网站，现在的网站只关心流量。但是反过来，网站就需要证明自己的身份了。
比如说现在钓鱼网站很多的，比如你想访问的是www.baidu.com，但其实你访问的是www.daibu.com”，所以在提交自己的隐私信息之前需要验证一下网站的身份，要求网站出示数字证书。
一般正常的网站都会主动出示自己的数字证书，来确保客户端和网站服务器之间的通信数据是加密安全的。

3 案例
3.1 访问SSL证书正常网站
import requests
# response = requests.get("https://www.baidu.com/", verify=True)
# 也可以省略不写#
response = requests.get("https://www.baidu.com/")
print(response.content.decode("utf-8"))
运行结果：



3.2 代码访问带有CA认证的网站
来测试一下：
import requests
response = requests.get("https://www.12306.cn/mormhweb/")
print(response.text)
果然：

SSLError: ("bad handshake: Error([('SSL routines', 'ssl3_get_server_certificate', 'certificate verify failed')],)",)

如果SSL证书验证不通过，或者不信任服务器的安全证书，则会报出SSLError，据说 12306 证书是自己做的：

3.3 跳过 12306 的证书验证
 Requests也可以为HTTPS请求验证SSL证书，要想检查某个主机的SSL证书，你可以使用 verify 参数，把 verify 设置为 False 就可以正常请求了。忽略验证证书。
import requests
response = requests.get("https://www.12306.cn/mormhweb/", verify = False)
print(response.content.decode("utf-8"))

运行效果：


9.下载图片
1. 案例--下载没有反爬虫的图片

把这张图片下载下来：

import requests
#图片地址
response = requests.get("http://www.atguigu.com/images/logo.jpg")
#打印响应码
print("code==",response.status_code)
if response.status_code == 200:
    #保存图片名字为logo.jpg
    with open('logo.jpg', 'wb') as f:
        f.write(response.content)

运行效果如下：

2 案例--下载有反爬虫的图片
http://www.meizitu.com/
在浏览器能够正常显示

http://mm.chinasareview.com/wp-content/uploads/2017a/07/18/07.jpg
在浏览器能够正常显示


同样代码，换图片链接下载不下来，反馈图片没有找到

添加请求头信息全面模拟浏览器

用正则匹配处理请求头信息
正则表达式：
^(.*): (.*)$
"\1":"\2",

完整代码
注意事项，红色部分没有空格哦

import requests

#图片地址
image_url = "http://mm.chinasareview.com/wp-content/uploads/2017a/07/18/07.jpg"
headers = {

"Host":"mm.chinasareview.com",
"Proxy-Connection":"keep-alive",
"Cache-Control":"max-age=0",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.9",
"Cookie":"__jsluid=6dad86b537349828028bbed3237da97a",
"If-None-Match": "f67cd360b83ed31:104f",
"If-Modified-Since": "Fri, 06 Oct 2017 15:32:54 GMT",
}
response = requests.get(image_url,headers=headers)
#打印响应码
print("code==",response.status_code)
if response.status_code == 200:
    #保存图片名字为logo.jpg
    with open('logo.jpg', 'wb') as f:
        f.write(response.content)

运行结果得到图片了：


保存图片优化代码
如果一个文件很大，比如5G，试想应该怎样把文件的数据读取到内存然后进行处理呢？

print("code==",response.status_code)
if response.status_code == 200:
   #保存图片名字为logo.jpg
   with open('logo.jpg', 'wb') as f:
      for block in response.iter_content(1024):
         #判断是否还有内容,没有就退出for循环
         if not block:
            break
         #把取出的内容写入文件
         f.write(block)


10. 综合案例--批量爬取贴吧页面数据
需求：简单写一个小爬虫程序，来爬取百度尚硅谷吧的所有网页。


1 百度贴吧url分析
首先我们创建一个python文件, 百度贴吧爬虫.py，我们要完成的是，输入一个百度贴吧的地址，比如：
百度贴吧尚硅谷吧第一页：
https://tieba.baidu.com/f?kw=尚硅谷pn=0
第二页： 
https://tieba.baidu.com/f?kw=尚硅谷pn=1
第三页：
https://tieba.baidu.com/f?kw=尚硅谷pn=2
发现规律了吧，贴吧中每个页面不同之处，就是url最后的pn的值，其余的都是一样的，我们可以抓住这个规律。
先写一个main，提示用户输入要爬取的贴吧名，并用parse.urlencode进行转码，然后组合url，假设是尚硅谷吧，那么组合后的url就是：http://tieba.baidu.com/f?kw=尚硅谷

if __name__ == "__main__":
   kw = input("请输入你要爬取的贴吧名称：")
   start_page = int(input("请输入起始页："))
   end_page = int(input("请输入结束页面："))

   kw = {"kw":kw}
   
   url = "https://tieba.baidu.com/f?"

   print(url)
   

运行效果：

2 百度贴吧url组拼

接下来，我们写一个百度贴吧爬虫接口，我们需要传递3个参数给这个接口， 一个是main里组合的url地址，以及起始页码和终止页码，表示要爬取页码的范围。

#组拼1~6页的连接
def tieba_spide(url,start_page,end_page):
   """

   :param url: 爬虫的爬取的主路径
   :param start_page: 爬虫的爬取的起始页
   :param end_page: 爬虫的爬取的结束始页
   :return:
   """
   for page in range(start_page,end_page+1):
   #每页50条数据：根据数据库分页公式：select * from students where limit (n-1)*m ,m
   #(n-1)*m是起始数据；m是每页多少条数据
      pn = (page-1) * 50

      full_url = url+"&pn="+ str(pn)
      print(full_url)


if __name__ == "__main__":
   kw = input("请输入你要爬取的贴吧名称：")
   start_page = int(input("请输入起始页："))
   end_page = int(input("请输入结束页面："))

   kw = {"kw":kw}


   url = "https://tieba.baidu.com/f?"

   # print(url)
   #组装1~6页的数据
   tieba_spide(url,start_page,end_page)

运行效果：

3 根据url请求数据

我们已经之前写出一个爬取一个网页的代码。现在，我们可以将它封装成一个小函数load_page，供我们使用。
import requests

def load_page(full_url,file_name,kw):
   print("正在下载：%s" % file_name)
   headers = {
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
   # 打开连接
   response = requests.get(full_url,headers=headers,params=kw)
   #返回数据
   return response.text


#组拼1~6页的连接
def tieba_spide(url,start_page,end_page,kw):
   """

   :param url: 爬虫的爬取的主路径
   :param start_page: 爬虫的爬取的起始页
   :param end_page: 爬虫的爬取的结束始页
   :return:
   """
   for page in range(start_page,end_page+1):
      #每页50条数据：根据数据库分页公式：select * from students where limit (n-1)*m ,m
      #(n-1)*m是起始数据；m是每页多少条数据
      pn = (page-1) * 50

      full_url = url+"&pn="+ str(pn)
      #文件名称
      file_name = "第"+str(page) +"页.html"
      print("full_url==",full_url)

      response_data = load_page(full_url,file_name,kw)
      print(response_data)


if __name__ == "__main__":
   kw = input("请输入你要爬取的贴吧名称：")
   start_page = int(input("请输入起始页："))
   end_page = int(input("请输入结束页面："))

   kw = {"kw":kw}

   url = "https://tieba.baidu.com/f?"

   #组装1~6页的数据
   tieba_spide(url,start_page,end_page,kw)

运行效果：


4 保存数据到本地磁盘上

最后如果我们希望将爬取到了每页的信息存储在本地磁盘上，我们可以简单写一个存储文件的接口。
你可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险：
import requests
#保存文件
def writ_file(html,file_name):
   print("正在保存：%s" % file_name)

   #这种写法不用去关闭，帮我们关闭
   with open(file_name,"wb") as f:
      f.write(html)

   print("--"*20)


#请求网络
def load_page(full_url,file_name,kw):
   print("正在下载：%s" % file_name)
   headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
   response = requests.get(full_url,headers=headers,params=kw)
   #返回数据
   return response.content


#组拼1~6页的连接
def tieba_spide(url,start_page,end_page,kw):
   """

   :param url: 爬虫的爬取的主路径
   :param start_page: 爬虫的爬取的起始页
   :param end_page: 爬虫的爬取的结束始页
   :return:
   """
   for page in range(start_page,end_page+1):
      #每页50条数据：根据数据库分页公式：select * from students where limit (n-1)*m ,m
      #(n-1)*m是起始数据；m是每页多少条数据
      pn = (page-1) * 50

      full_url = url+"&pn="+ str(pn)
      #文件名称
      file_name = "第"+str(page) +"页.html"
      print("full_url==",full_url)

      response_data = load_page(full_url,file_name,kw)
      print(response_data)
      writ_file(response_data,file_name)


if __name__ == "__main__":
   kw = input("请输入你要爬取的贴吧名称：")
   start_page = int(input("请输入起始页："))
   end_page = int(input("请输入结束页面："))

   kw = {"kw":kw}


   url = "https://tieba.baidu.com/f?"

   url = url
   # print("url==",url)
   #组装1~6页的数据
   tieba_spide(url,start_page,end_page,kw)
其实很多网站都是这样的，同类网站下的html页面编号，分别对应网址后的网页序号，只要发现规律就可以批量爬取页面了。
