import requests
r=requests.get('https://www.taobao.com/')
with open('taobao.html', 'wb') as f:
    f.write(r.content)
# print(r.text)
# print(r.json())
# print(r.cookies('245531198@qq.com'))