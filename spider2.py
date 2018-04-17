from urllib import request
from urllib.error import HTTPError, URLError

try:
    request.urlopen("http://blog.csdnm.net")
except HTTPError as e:
    print(e.code)
    print(e.reason)
except URLError as e:
    print(e.reason)
