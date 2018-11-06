from urllib import request, parse
import json


def get_response(ur, word):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
    }
    # http: // fy.iciba.com / ajax.php?a = fy
    data = {
        'f': 'auto',
        't': 'auto',
        'w': word,
    }
    da = bytes(parse.urlencode(data), encoding='utf-8')
    response = request.Request(url=ur, headers=headers, data=da)
    print(response)
    return response


def parse_one_page(response):
    content = request.urlopen(response).read().decode('utf-8')
    return content


def main(word):
    url = 'http://fy.iciba.com/ajax.php?a=fy'
    response = get_response(url, word)
    content = parse_one_page(response)
    print(json.loads(content))
    for i in json.loads(content)['content']['out']:
        print(i,end='')
    print()


if __name__ == '__main__':
    while True:
        word = input('请输入单词：')
        main(word)


