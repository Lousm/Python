from urllib import request,parse
url='http://httpbin.org/post'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Host':'httpbin.org'
}
dict={
    'name':'henankejixueyuan'
}
data=bytes(parse.urlencode(dict).encode('utf-8'))
req=request.Request(url=url,data=data,headers=headers,method='POST')
response=request.urlopen(req)
print(response.read().decode('utf-8'))