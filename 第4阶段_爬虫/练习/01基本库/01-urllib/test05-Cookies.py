import urllib.request
import http.cookiejar

# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# # response=opener.open('http://10.10.91.184:8000/student_manage/show')
# for item in cookie:
#     print(item.name+"="+item.value)

# filename='cookers.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# # response=opener.open('http://10.10.91.184:8000/student_manage/show')
# cookie.save(ignore_discard=True,ignore_expires=True)

filename='cookers2.txt'
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
# response=opener.open('http://10.10.91.184:8000/student_manage/show')
cookie.save(ignore_discard=True,ignore_expires=True)
