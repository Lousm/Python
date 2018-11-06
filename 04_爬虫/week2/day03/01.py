import requests

res = requests.get('http://langlang2017.com')
print(res.encoding)
print(res.text.encode('ISO-8859-1').decode('utf-8'))
print(res.apparent_encoding)

