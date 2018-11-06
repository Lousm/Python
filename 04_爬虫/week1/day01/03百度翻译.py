from urllib import request, parse
import json


def get_content(ur, word):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
    }
    # https: // fanyi.baidu.com/sug
    data = {
        'kw': word,
    }
    da = bytes(parse.urlencode(data), encoding='utf-8')
    response = request.Request(url=ur, headers=headers, data=da)
    content = request.urlopen(response).read().decode('utf-8')
    print(content)
    return content


def main(word):
    url = 'https://fanyi.baidu.com/sug'
    content = get_content(url, word)
    print(json.loads(content))

    for item in json.loads(content)['data']:
        print(item['v'])


if __name__ == '__main__':
    while True:
        word = input('请输入单词：')
        main(word)
