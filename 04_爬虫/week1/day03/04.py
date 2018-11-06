import requests

res=requests.get('http://langlang2017.com/img/logo.png')
with open('logo.png','wb') as f:
    f.write(res.content)