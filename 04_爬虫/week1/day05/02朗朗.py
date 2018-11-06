import requests
from bs4 import BeautifulSoup

url = 'http://langlang2017.com/'

con = requests.get(url).content

soup = BeautifulSoup(con, 'lxml')

# 获取最外层div下得每一个div
div_list = soup.select('div[class="pinzhibaozhang_center"] div')
# print(div_list)
for i in div_list:

    #获取每个div下面的所有子节点
    div_children = i.children

    # 遍历每个节点
    for j in div_children:
        if j != '\n':
            print(j)

            #获取每个节点的属性
            attrs=j.attrs
            if 'src' in attrs:
                print(attrs)

            #获取每个节点的值
            print(j.get_text().strip())
