import requests
from bs4 import BeautifulSoup

url = 'https://www.shanbay.com/wordlist//110521/232414/?page=1'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
}

con = requests.get(url=url, headers=headers).content

soup = BeautifulSoup(con, 'lxml')

tr_list = soup.select('tr[class="row"]')

items = []
for i in tr_list:
    # print(i)
    item = {}
    yingwen = i.select('td')[0].get_text()
    hanyu = i.select('td')[1].get_text()
    item['英文']=yingwen
    item['翻译']=hanyu

    items.append(item)

print(items)
