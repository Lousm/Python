from urllib import request,parse
from http import cookiejar
import ssl
ssl._create_default_https_context=ssl._create_stdlib_context

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
    }

cookie=cookiejar.CookieJar()
cookie_handler=request.HTTPCookieProcessor(cookie)
http_handler=request.HTTPHandler()
https_handler=request.HTTPSHandler()
opner=request.build_opener(http_handler,https_handler,cookie_handler)


def login():
    url='https://security.kaixin001.com/login/login_post.php'
    data={
        'email':'18811176939',
        'password':'123457',

    }

    data=bytes(parse.urlencode(data),encoding='utf-8')
    res=request.Request(url=url,data=data)

    response=opner.open(res)

def getpage():
    url='http://www.kaixin001.com/home/index.php'
    content=opner.open(url).read().decode('utf-8')
    print(content)

if __name__ == '__main__':
    login()
    getpage()
