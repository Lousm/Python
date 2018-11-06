import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
}
url = 'https://api.bilibili.com/x/v1/dm/list.so?oid=58659251'
con = requests.get(url=url, headers=headers, verify=False).content
print(con)
tree = etree.HTML(con)
d_list = tree.xpath('//d')
for i in d_list:
    tex = i.xpath('./text()')
    print(tex)
    with open('弹幕.txt', 'a', encoding='utf-8') as f:
        f.write(tex[0]+'\n')
