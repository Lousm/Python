from urllib import request, parse


def get_response(ur, name, page):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
    }
    data = {
        'ie': 'utf-8',
        'kw': name,
        'pn': page,
    }
    url = ur + parse.urlencode(data)
    response = request.Request(url=url, headers=headers)
    return response


def parse_one_page(response):
    content = request.urlopen(response).read().decode('utf-8')
    return content


def write_to_file(content, name, page):
    with open('%s第%d页.html' % (name, page), 'w+', encoding='utf-8') as f:
        f.write(content)


def main(name, page):
    url = 'http://tieba.baidu.com/f?'
    response = get_response(url, name, page=page * 50)
    content = parse_one_page(response)
    write_to_file(content, name, page=page + 1)


if __name__ == '__main__':
    name = input('请输入贴吧名称：')
    for i in range(10):
        main(name, i)
