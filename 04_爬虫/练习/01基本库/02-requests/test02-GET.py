import requests
import re
# r=requests.get('http://httpbin.org/get')
# print(r.text)

# data={
#     'name':'xiaoming',
#     'age':55
# }
# r=requests.get('http://httpbin.org/get',params=data)
# print(r.text)
# print(r.json)

# headers={
#     'User-Agent:Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'
# }
# r=requests.get('https://www.zhihu.com/explore',headers=headers)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
# titles=re.findall(pattern,r.text)
# print(titles)

# r=requests.get('https://github.com/favicon.ico')
# # print(r.text)
# # print(r.content)
# with open('favicon.ico','wb') as f:
#     f.write(r.content)

# r=requests.get('https://www.zhihu.com/explore')
# print(r.text)

data={
    'name':'xiaoming',
    'age':55
}
r=requests.post('http://httpbin.org/post',data=data)
print(r.text)