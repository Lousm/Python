import requests, re

res = requests.get('http://langlang2017.com')
html = res.text.encode('ISO-8859-1').decode(res.apparent_encoding)
# print(html)
pattern = re.compile('<li><img.*?src="img/(.*?)"', re.S)
con = re.findall(pattern, html)
print(con)

for i in con[0]:
    ur = 'http://langlang2017.com/img/' + i
    r = requests.get(ur)
    with open(i, 'wb') as f:
        f.write(r.content)
