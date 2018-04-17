from urllib import request, error
import re
import time
import threading
import queue

headers = ("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0")
opener = request.build_opener()
opener.addheaders = [headers]
request.install_opener(opener)
listurl = []
urlqueue = queue.Queue()


def use_proxy(proxy_address, url):
    try:
        proxy = request.ProxyHandler({"http": proxy_address})
        opener = request.build_opener(proxy, request.HTTPHandler)
        request.install_opener(opener)
        data = request.urlopen(url).read().decode("utf-8")
        return data
    except error.URLError as e:
        if hasattr(e, "code:"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
        time.sleep(10)
    except Exception as  e:
        print("exception:" + str(e))
        time.sleep(1)


class geturl(threading.Thread):
    def __init__(self, key, pagestart, pageend, proxy, urlqueue):
        threading.Thread.__init__(self)
        self.pagestart = pagestart
        self.pageend = pageend
        self.proxy = proxy
        self.key = key
        self.urlqueue = urlqueue

    def run(self):
        page = self.pagestart
        keycode = request.quote(self.key)
        pagecode = request.quote("&page")
        for page in range(self.pagestart, self.pageend + 1):
            url = "http://weixin.sogou.com/weixin?query=" + keycode + "&type=2" + pagecode + str(page)
            data1 = use_proxy(self.proxy, url)
            listurlpat = '<div class="txt-box">\t<h3>\t<a target="_blank" href="(http://.*?)"'
            listurl.append(re.compile(listurlpat, re.S).findall(data1))
        print("共获取到" + str(len(listurl)) + "页")
        for i in range(0, len(listurl)):
            time.sleep(7)
            for j in range(0, len(listurl[i])):
                try:
                    url = listurl[i][j]
                    url = url.replace("amp", "")
                    print("第" + str(i) + "i" + str(j) + "j次入队")
                    self.urlqueue.put(url)
                    self.urlqueue.task_done()
                except error.URLError as  e:
                    if hasattr(e, "code"):
                        print(e.code)
                    if hasattr(e, "reason"):
                        print(e.reason)
                    time.sleep(10)
                except Exception as  e:
                    print("exception:" + str(e))
                    time.sleep(1)


class getcontent(threading.Thread):
    def __init__(self, urlqueue, proxy):
        threading.Thread.__init__(self)
        self.urlqueue = urlqueue
        self.proxy = proxy

    def run(self):
        html1 = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\t<html xmlns="http://www.w3.org/1999/xhtml">\t<head>\t<meta\t http-equiv="Content-Type"\tcontent="text/html"\tcharset = "UTF-8">\t <title> 微信文章页面 </title >\t</head >\t<body>'
        fh = open("C:\\Users\\ZhangChenglong.HDSC\\PycharmProjects\\spark\\static\\5.html", "wb")
        fh.write(html1.encode("utf-8"))
        fh.close()
        fh = open("C:\\Users\\ZhangChenglong.HDSC\\PycharmProjects\\spark\\static\\5.html", "ab")
        for i in range(0, len(listurl)):
            for j in range(0, len(listurl[i])):
                try:
                    url = listurl[i][j]
                    url = url.replace("amp", "")
                    data = use_proxy(self.proxy, url)
                    titlepat = '<title>(.*?)</title>'
                    title = re.compile(titlepat, re.S).findall(data)
                    contentpat = '<div class="rich_media_content " id="js_content">(.*?)<div class="rich_media_tool" id="js_sg_bar">'
                    content = re.compile(contentpat, re.S).findall(data)
                    thistitle = "此次没有获取到"
                    thiscontent = "此次没有获取到"
                    if (title != []):
                        thistitle = title[0]
                    if (content != []):
                        thiscontent = content[0]
                    dataall = '<p>标题是:' + thistitle + '</p><p>内容是:' + thiscontent + '</p>'
                    fh.write(dataall.encode("utf-8"))
                    print("第" + str(i) + "个网页" + str(j) + "次处理")
                except error.URLError as e:
                    if hasattr(e, "code"):
                        print(e.code)
                    if hasattr(e, "reason"):
                        print(e.reason)
                    time.sleep(10)
                except Exception as e:
                    print("exception:" + str(e))
                    time.sleep(1)
            fh.close()
            html2 = '</body>\t</html>'
            fh = open("C:\\Users\\ZhangChenglong.HDSC\\PycharmProjects\\spark\\static\\5.html", "ab")
            fh.write(html2.encode("utf-8"))
            fh.close()


class control(threading.Thread):
    def __init__(self, urlqueue):
        threading.Thread.__init__(self)
        self.urlqueque = urlqueue

    def run(self):
        while (True):
            print("程序执行中")
            time.sleep(60)
            if (self.urlqueque.empty()):
                print("程序执行完毕")
                exit()


t1 = geturl("人工智能", pagestart=1, pageend=2, proxy="61.135.217.7:80", urlqueue=urlqueue)
t1.start()
t2 = getcontent(urlqueue=urlqueue, proxy="61.135.217.7:80")
t2.start()
t3 = control(urlqueue=urlqueue)
t3.start()
