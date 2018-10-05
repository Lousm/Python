import urllib.request
response = urllib.request.urlopen('http://10.10.91.184:8000/student_manage/show')
# print(response.read().decode('utf-8'))
print(type(response))
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))
