import urllib.request
import urllib.parse


# keyword = 'Java线程安全'
# url = "https://www.baidu.com/s?wd="
# User_Agent = 'User-Agent'
# brow = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:59.0) Gecko/20100"
# req = urllib.request.Request(url + urllib.request.quote(keyword))
# req.add_header(User_Agent, brow)
# data = urllib.request.urlopen(req).read()
# file = open("C:\\Users\\ZhangChenglong.HDSC\\PycharmProjects\\spark\\static\\3.html", 'wb')
# file.write(data)
# file.close()

# url = "http://www.iqianyue.com/mypost"
# UserAgent = 'User-Agent'
# Brower = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:59.0) Gecko/20100"
# postdata = urllib.parse.urlencode({'name': "zhangsan", "pass": "admin123"}).encode("utf-8")
# req = urllib.request.Request(url, postdata)
# req.add_header(UserAgent, Brower)
# data = urllib.request.urlopen(req).read()
# file = open("C:\\Users\\ZhangChenglong.HDSC\\PycharmProjects\\spark\\static\\4.html", 'wb')
# file.write(data)
# file.close()


def user_proxy(address, url):
    import urllib.request
    httphd = urllib.request.HTTPHandler(debuglevel=1)
    httpshd = urllib.request.HTTPSHandler(debuglevel=1)
    proxy = urllib.request.ProxyHandler({"http": address})
    opener = urllib.request.build_opener(proxy, httphd, httpshd)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode('utf-8')
    return data


print(len(user_proxy("120.92.117.94:10000", "http://www.baidu.com")))
