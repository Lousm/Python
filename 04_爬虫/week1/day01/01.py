import urllib


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
}
url = 'https://www.baidu.com'
res = urllib.request.Request(url=url, headers=headers)
content = urllib.request.urlopen(res)

with open('baidu.html', 'w', encoding='utf-8') as f:
    f.write(content.read().decode('utf-8'))
