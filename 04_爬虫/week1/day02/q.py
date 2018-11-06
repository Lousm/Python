import requests, urllib

res = requests.get('https://bbs.zgfriends.club/thread-18-1-1.html')
# print(res.text)

re = urllib.request.urlopen('https://bbs.zgfriends.club/thread-18-1-1.html')
print(re.read().decode('utf-8'))
