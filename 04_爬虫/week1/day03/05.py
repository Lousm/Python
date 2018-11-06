import requests

url = 'http://www.renren.com/PLogin.do'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
}

data = {
    'email': '17739115043',
    'password': 'ying0229._'
}

s = requests.session()  # 生成一个session对象
s.post(url=url, data=data, headers=headers)  # 请求登陆页面时，cookie已经保存到session对象中去了

res = s.get('http://www.renren.com/968293383/profile')

with open('renren.html', 'w', encoding='utf-8') as f:
    f.write(res.text)
