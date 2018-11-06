import requests
import re
import urllib3
# files={
#     'file':open('favicon.ico','rb')
# }
# r=requests.post('http://httpbin.org/post',files=files)
# print(r.text)

# heard={
#     'Cookie':'_zap=571a3678-d3b5-4330-ac38-97dda7f515fd; d_c0="AIAlSHUXrA2PTsU6aDehNswsiWMxzwEhTcY=|1527667173"; _xsrf=OQlCo02s0w830IIlNlyjxhYvcYS0LM8o; tgw_l7_route=bc9380c810e0cf40598c1a7b1459f027; capsion_ticket="2|1:0|10:1538895469|14:capsion_ticket|44:MjRiMzI3YTQxOWYzNDYxZGI3OWI0NzYzZWViODZkZTI=|9fccd36085d57cf9ecdc00f8a0040259167d885af581db693e3ed91ac9379221"; z_c0="2|1:0|10:1538895592|4:z_c0|92:Mi4xYmFzc0RBQUFBQUFBZ0NWSWRSZXNEU2NBQUFDRUFsVk42RHZoV3dBLTNSSndRSG5GU2VkWGk5OXMtVFB5TDZkWUx3|0b1342564f84ed08db1ca895e4e2f006788d11f4890fbcfd2faa4112972ab1b1"; q_c1=4d442d7e84024bd5ad3b72c49a1a53d5|1538895592000|1525882053000',
#     'Host':'www.zhihu.com',
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
# }
# r=requests.get('https://www.zhihu.com',headers=heard)
# print(r.text)

# urllib3.disable_warnings
# r=requests.get('https://www.12306.cn',verify=False)
# print(r.status_code)


html = '''<div id = "songs-list" > 
<h2 class = "title" > 経 典老歌 < /h2 > くp class = "introduction" > 経典老歌列表 < /p >
<ul id = "list" class = "list-group" > <li data-view = "2" > 一路 上有价 < /li > <li data-view = "7" >
<a href = "/2.mp3" singer ="任賢斉"> 洽海一声笑 < /a > </li >
<li data-view = "4" class = " active" >
<a href = "/3.mp3" singer ="斉秦"> 往事随凡 </a> </li >
<li data-view = "6" > <a> href = " /4.mp3" singer = "beyond" > 光輝劣月 < /a > 
</li > <li data-view = "5" > <a href = "/5.mp3" singer = " 除慧琳" > 記事本 < /a > 
</li > <li data-view = "5" >
<a href = "/6.mp3" singer =" 那萠君"> 但愿人天久 < /a > </1i > </ul >
</div >'''

# res = re.search('<li.*?active.*?singer.*?="(.*?)".*?>.*?(.*?)</a>', html, re.S)
# if res:
#     print(res.group(1),res.group(2))

# res = re.findall('href.*?=.*?"(.*?)".*?singer.*?=.*?"(.*?)".*?>(.*?)<.*?/a.*?>', html)
# if res:
#     print(res)

htm=re.sub('<.?a.*?>|<.?/a.?>','',html)
# print(htm)
res=re.findall('<li.*?>(.*?)<.?/li.?>',htm,re.S)
print(res)
