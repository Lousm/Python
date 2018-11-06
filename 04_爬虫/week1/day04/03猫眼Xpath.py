import requests, re
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
}

res = requests.get('http://maoyan.com/board/7', headers=headers).content.decode('utf-8')
tree = etree.HTML(res)

dd_list = tree.xpath('//dd')
# print(dd_list)

for dd in dd_list:
    pm = dd.xpath(
        './i[1]/text()|.//p[1]/a/text()|.//p[@class="star"]/text()|.//p[@class="releasetime"]/text()|.//i[@class="integer"]/text()|.//i[@class="fraction"]/text()|.//img[@data-src]/@data-src')
    print(re.sub('\n| ', '', str(pm)))
    # for i in pm:
    #     i = re.sub('\\n| ', '', i)#去掉换行符和空格
    #     print(i)
    print()

