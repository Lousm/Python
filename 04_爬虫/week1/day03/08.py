import requests, re

res = requests.get('http://langlang2017.com')
html = res.text.encode('ISO-8859-1').decode(res.apparent_encoding)
# print(html)
pattern1 = re.compile('<li><img.*?alt="(.*?)".*?src="img/(.*?)"', re.S)

pattern2 = re.compile('href="(h.*?)"', re.S)

pattern3 = re.compile('class="beian">(.*?)<.*?href="(.*?)".*?BABCBD;">(.*?)</a>', re.S)
con1 = re.findall(pattern1, html)
con2 = re.findall(pattern2, html)
con3 = re.findall(pattern3, html)
print(con1)
print(con2)
print(con3)
# for i in con1:
#     # ur = 'http://langlang2017.com/img/' + i
#     # r = requests.get(ur)
#     print(i)
# for i in con2:
#     # ur = 'http://langlang2017.com/img/' + i
#     # r = requests.get(ur)
#     print(i)
