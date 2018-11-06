import urllib

try:
    res=urllib.request.urlopen('http://www.baidu.cm/sfsfs')

except urllib.error.HTTPError as e:
    print(e.reason)

except urllib.error.URLError as e:
    print(e.reason)

else:
    print(res)

