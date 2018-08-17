from urllib import request
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data=f.read()
    print('状态：',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s:%s'%(k,v))
    print('数据：',data.decode('Utf-8'))
