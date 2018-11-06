import requests
from bs4 import BeautifulSoup

url = 'http://langlang2017.com/'
con = requests.get(url).content

soup = BeautifulSoup(con, 'lxml')
# print(soup.name)
# print(soup.title.name)
# print(soup.title.attrs)
# print(soup.title.string)
# print(soup.title)
print(soup.a)
# print(soup.img.attrs)


# print(soup.a)
# con = soup.prettify()
# print(con)
# print(soup.title.contents)
#
# print(soup.title.children)
# for i in soup.head.children:
#     print(i)
# for i in soup.div.children:
#     print(i)
#
# print('---------------------------------')
# for i in soup.div.descendants:
#     print(i)

# print(soup.find_all('a'))
print(soup.find_all(id ="weixin"))
