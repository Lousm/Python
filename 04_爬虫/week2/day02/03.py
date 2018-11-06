import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
}
url = 'https://api.bilibili.com/x/v1/dm/list.so?oid=59392645'
con = requests.get(url=url, headers=headers, verify=False).content.decode('utf-8')

pattern = re.compile('<d.*?>(.*?)<', re.S)

t = re.findall(pattern, con)

for i in t:
    with open('弹幕3000（正则）.txt', 'a', encoding='utf-8') as f:
        f.write(i + '\n')

print(t)
