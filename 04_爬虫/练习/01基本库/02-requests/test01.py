import requests
r=requests.get('https://ww.baidu.com')
print(type(r))
print(r.status_code)
print(r.text)
print(type(r.text))
print(r.cookies)