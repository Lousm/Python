import requests
from lxml import etree

con = requests.get('http://langlang2017.com/').content.decode('utf-8')

tree = etree.HTML(con)

res = tree.xpath('//div[@class="dizhi"]/text()')

r2=tree.xpath('//div[@class="beian"]/text()')
r2=tree.xpath('//div[@class="beian"]/text()')
r3=tree.xpath('//div[@class="beian"]/a/@href')
r4=tree.xpath('//div[@class="beian"]/a/text()')
r5=tree.xpath('//div[@class="banner_box"]//li//@src')

print(res)
print(r2)
print(r3)
print(r4)
print(r5)
