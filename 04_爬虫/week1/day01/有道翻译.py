from urllib import request, parse
import json, time, hashlib, random


def get_content(ur, word):
    u = 'fanyideskweb'
    d = word  # 输入的单词
    f = str(int(time.time() * 1000) + random.randint(0, 10))  # 时间戳
    c = '6x(ZHw]mwzX#u0V7@yfwK'
    s = u + d + f + c
    sign = get_md5(s)  # 四个参数连接起来的MD5加密值

    print(f)
    print(sign)
    data = {
        'i': word,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': f,
        'sign': sign,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typoResult': 'false',
    }
    da = bytes(parse.urlencode(data).encode('utf-8'))
    Content_Length = len(da)
    print(Content_Length)

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': Content_Length,  # data的长度
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; OUTFOX_SEARCH_USER_ID=147654701@221.220.96.2; JSESSIONID=abczyGnbdOjJ0flsoYtzw; OUTFOX_SEARCH_USER_ID_NCOO=1899489274.917913; _ntes_nnid=b0185baf8c95e24b6bd56fa8c46779b3,1539003975430; ___rl__test__cookies=1539010274867',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http://fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com/?keyfrom=fanyi-new.logo',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    response = request.Request(url=ur, headers=headers, data=da, method='POST')
    content = request.urlopen(response).read().decode('utf-8')
    return content


# MD5加密
def get_md5(v):
    md5 = hashlib.md5()
    md5.update(v.encode('utf-8'))
    value = md5.hexdigest()
    return value


def main(word):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    content = get_content(url, word)
    print(content)


if __name__ == '__main__':
    while True:
        word = input('请输入单词：')
        main(word)
