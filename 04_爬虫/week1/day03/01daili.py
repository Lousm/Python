from urllib import request
import requests,random

list=[
    {'https': '61.163.37.22:58772'},
    {'https': '106.75.164.15:3128'}
]

proxies =random.choice(list)
print(proxies)
res = requests.get('http://httpbin.org/get', proxies=proxies)

# proxies_hand=request.ProxyHandler(proxies)
#
# opener=request.build_opener(proxies_hand)
#
# res1=opener.open('http://httpbin.org/get')
#
# print(res1.read().decode('utf-8'))
print(res.text)