from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import etree
import json

drive = webdriver.PhantomJS(
    executable_path=r'C:\Users\Mr_Lou\Desktop\新建文件夹 (2)\phantomjs-2.1.1-windows\bin\phantomjs.exe')

url = 'https://book.douban.com/subject_search?search_text=python&cat=1001'

drive.get(url)

tree = etree.HTML(drive.page_source)

book_list = tree.xpath('//div[@class="item-root"]')
print(book_list)
items=[]
for i in book_list:
    name = i.xpath('.//a/img/@alt')
    print(name)
    pingfen=i.xpath('.//span[@class="rating_nums"]/text()')
    print(pingfen)
    num=i.xpath('.//span[@class="pl"]/text()')
    jianjie=i.xpath('.//div[@class="meta abstract"]/text()')
    item={}
    item['书名']=name
    item['评分']=pingfen
    item['评价人数']=num
    item['简介']=jianjie
    items.append(item)

data=json.dumps(items,ensure_ascii=False)
with open('豆瓣读书.json','w',encoding='utf-8') as f:
    f.write(data)

