from urllib import request
import re


def getlink(url):
    header = ("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0")
    opener = request.build_opener()
    opener.addheaders = [header]
    request.install_opener(opener)
    file = request.urlopen(url)
    data = str(file.read())
    pattern = '(https?://[^\s)";]+\.(\w|/)*)"'
    link = re.compile(pattern).findall(data)
    link = list(set(link))
    return link


for link in getlink("https://www.zhihu.com/"):
    print(link[0])