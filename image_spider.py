import re
import urllib.request


def craw(url, page):
    html1 = urllib.request.urlopen(url).read()
    html1 = str(html1)
    # print(html1)
    part1 = '<div id="J_goodsList".+?<div id="J_scroll_loading"'
    result1 = re.compile(part1).findall(html1)
    result1 = result1[0]
    part2 = '<img width="220" height="220" class="err-product" data-img="1" src="//(.+?\.jpg)" />'
    imagelist = re.compile(part2).findall(result1)
    print(imagelist[0])
    x = 1
    for imageurl in imagelist:
        imagename = "D:/picture/" + str(page) + str(x) + ".jpg"
        imageurl = "http://" + imageurl
        print(imageurl)
        try:
            urllib.request.urlretrieve(imageurl, filename=imagename)
        except urllib.request.URLError as e:
            if hasattr(e, "code"):
                x += 1
            if hasattr(e, "reason"):
                x += 1
        x += 1



# craw("https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=3&s=56&click=0",3)

for i in range(3, 79, 2):
    url = "https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=" + str(
        i) + "&s=56&click=0"
    craw(url, i)
