import requests

r=requests.get('http://www.runoob.com/python/python-reg-expressions.html')
print(r.status_code)
print(r.url)
print(r.encoding)
print(r.content)