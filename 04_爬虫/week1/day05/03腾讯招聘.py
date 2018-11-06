import requests, json
from bs4 import BeautifulSoup

url = 'https://hr.tencent.com/position.php'

data = {
    'keywords': 'python',
    'lid': '2156',  # 所在位置代号
    'tid': '0',
    'start': '0'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
}

con = requests.get(url=url, headers=headers, params=data).content

# 构造bs4解析器
soup = BeautifulSoup(con, 'lxml')
print(con)

tr_list1 = soup.select('tr[class="even"]')
tr_list2 = soup.select('tr[class="odd"]')
tr_list = tr_list1 + tr_list2
print(tr_list)
items = []
for i in tr_list:
    name = i.select('td a')[0].get_text()
    href = i.select('td a')[0].attrs['href']
    exs = i.select('td')[1].get_text()
    pnum = i.select('td')[2].get_text()
    didian = i.select('td')[3].get_text()
    time = i.select('td')[4].get_text()
    # print(pnum)
    item = {}
    item['name'] = name
    item['href'] = 'https://hr.tencent.com/' + href
    item['exs'] = exs
    item['pnum'] = pnum
    item['didian'] = didian
    item['time'] = time

    items.append(item)
print(items)

data = json.dumps(items, ensure_ascii=False)
with open('tengxun.json', 'w', encoding='utf-8') as f:
    f.write(data)
