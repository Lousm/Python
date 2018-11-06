from urllib.parse import urlparse, urlunparse, urlencode,quote,unquote
# 连接解析

# result=urlparse('http://10.10.91.184:8000/shop/show_details/41')
# result=urlparse('https://www.baidu.com/s?wd=user-agent%E7%9A%84%E4%BD%9C%E7%94%A8&rsv_spt=1&rsv_iqid=0x89e5e33d00036c4f&issp=1&f=3&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=monline_3_dg&rsv_enter=1&rsv_t=e172Z%2FdeZJDCk2rleFJq6CBIumjyGdRpcu4hQ2OlkLSAugdbzly0gzDNxOr3celsZW2B&rsv_sug3=2&rsv_sug1=2&rsv_sug7=100&oq=User-Agent&rsv_pq=e5d5a4810001baf7&rsv_sug2=1&prefixsug=User-Agent&rsp=1&rsv_sug4=1574&rsv_sug=1')
# print(type(result),result)

# data=['http','www.asd.com','shop.html','username','name=zhangsan','asdas']
# print(urlunparse(data))

# a = {
#     'name': 'admin',
#     'pwd': 123456
# }
# base_url = 'http://www.baidu.com?'
# url = base_url+urlencode(a)
# print(url)

url='http://ww.baidu.com/s?wd=%CA%D6%BB%CA%BE%DD%CF%DF'
print(unquote(url))