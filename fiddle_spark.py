from urllib import request, error
import re
from http import cookiejar

url = "http://news.163.com/18/0416/15/DFH9NKMR000187V5.html"
refurl = "http://news.163.com/"
headers = {'Accept': ' text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Referer': refurl,
           'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0',
           'Accept-Encoding': 'utf-8', 'Connection': 'keep-alive'}
cjar = cookiejar.CookieJar()
proxy = request.ProxyHandler({"http": "127.0.0.1:8888"})
opener = request.build_opener(proxy, request.HTTPHandler, request.HTTPCookieProcessor(cjar))
headall = []
for k, v in headers.items():
    item = (k, v)
    headall.append(item)
opener.addheaders = headall
request.install_opener(opener)
data = request.urlopen(url=url).read()
fhandle = open("C:\\Users\\ZhangChenglong.HDSC\\PycharmProjects\\spark\\static\\7.html", 'wb')
fhandle.write(data)
fhandle.close()
