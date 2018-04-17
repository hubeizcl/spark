from urllib import request, error
import re
from http import cookiejar

vid = "1472528692"
comid = "6173403130078248384"
url = 'http://coral.qq.com/article/' + vid + 'comment?commentid=' + comid + "&reqnum=20"
headers = {'Accept': ' text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Referer': 'qq.com',
           'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0',
           'Accept-Encoding': 'utf-8', 'Connection': 'keep-alive'}
cjar = cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cjar))
handle = []
for k, v in headers.items():
    handle.append((k, v))

opener.addheaders = handle
request.install_opener(opener)


def craw(vid, comid):
    url = 'http://coral.qq.com/article/' + vid + 'comment?commentid=' + comid + "&reqnum=20"
    data = request.urlopen(url).read().decode('utf-8')
    return data


idpat = '"id":"(.*?)"'
userpat = '"nick":"(.*?)"'
conpat = '"content":"(.*?)"'
for i in range(0, 10):
    print("---------------------")
    print("第" + str(i) + "页评论")
    data = craw(vid, comid)
    idlist = re.compile(idpat, re.S).findall(data)
    userlist = re.compile(userpat, re.S).findall(data)
    contentlist = re.compile(conpat, re.S).findall(data)
    for i in range(0, len(userlist)):
        print("用户名是:" + userlist[i])
        print("评论内容是" + contentlist[i])
        print("\n")
    if idlist:
        comid = idlist[len(idlist)]
