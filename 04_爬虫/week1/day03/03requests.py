import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
}

data = {
    'wd': '河南科技学院'
}

url = 'https://www.baidu.com/s'
res = requests.get(url=url, params=data, headers=headers)
with open('河南科技学院.html', 'w',encoding='utf-8') as f:
    f.write(res.text)
