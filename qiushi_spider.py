# -*- coding: utf-8 -*-

from urllib import request
import re

header = ("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0")


def getcontent(proxy_address, url, page):
    proxy = request.ProxyHandler({"http": proxy_address})
    opener = request.build_opener(proxy, request.HTTPHandler)
    opener.addheaders = [header]
    request.install_opener(opener)
    data = request.urlopen(url).read().decode("utf-8")
    userpattern = ' target="_blank" title="(.*?)">\\t<h2>(.*?)</h2>'
    contentpattern = '<div class="content">(.*?)</div>'
    userlist = re.compile(userpattern, re.S).findall(data)
    contentlist = re.compile(contentpattern, re.S).findall(data)
    x = 1
    for content in contentlist:
        content = content.replace('\n', '')
        name = "content" + str(x)
        exec(name + "=content")
        x += 1
    y = 1
    for user in userlist:
        name = "content" + str(y)
        print("用户" + str(page) + str(y) + "是:" + user)
        print("内容是:")
        exec("print('+name+')")
        print("\n")
        y += 1


def getlink(url):
    opener = request.build_opener()
    opener.addheaders = [header]
    request.install_opener(opener)
    file = request.urlopen(url)
    data = str(file.read())
    pattern = '<a href="(/article/([0-9]+))"'
    link = re.compile(pattern).findall(data)
    link = list(set(link))
    return link


'''
 <td class="country"><img src="http://fs.xicidaili.com/images/flag/cn.png" alt="Cn" /></td>
    <td>27.37.47.47</td>
    <td>9797</td>
'''

for i in range(1, 30):
    urls = "https://www.qiushibaike.com/8hr/page/" + str(i) + "/"
    for url in getlink(urls):
        furl = "https://www.qiushibaike.com" + str(url[0])
        print(furl)
        getcontent("27.150.118.139:40103", furl, i)
