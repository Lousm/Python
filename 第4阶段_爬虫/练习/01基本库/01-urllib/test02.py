from urllib import request, parse,error
import socket
# data = bytes(parse.urlencode({'你好': 'hello'}).encode('utf-8'))
# response = request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())

# response = request.urlopen('http://httpbin.org/get', timeout=0.1)
# print(response.read())

try:
    response = request.urlopen('http://httpbin.org/get', timeout=0.1)
except error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('超时！')

