import requests, re, json, time


# 请求网页，返回响应体
def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None


def parse_noe_page(html):
    pa = re.compile('<tr.*?data-title="IP">(.*?)</td>'
                    + '.*?data-title="PORT">(.*?)</td>'
                    + '.*?data-title="匿名度">(.*?)</td>'
                    + '.*?data-title="类型">(.*?)</td>'
                    + '.*?data-title="位置">(.*?)</td>'
                    + '.*?data-title="响应速度">(.*?)</td>'
                    + '.*?data-title="最后验证时间">(.*?)</td>', re.S)
    res = re.findall(pa, html)
    # print(type(res))
    print(res)
    for i in res:
        yield {
            'IP': i[0],
            'PORT': i[1],
            '匿名度': i[2],
            '类型': i[3],
            '位置': i[4],
            '响应速度': i[5],
            '最后验证时间': i[6],
        }


# 将结果写入到文件
def write_to_file(content):
    with open('代理IP、端口号.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(num):
    url = 'https://www.kuaidaili.com/free/inha/' + num
    html = get_one_page(url)
    parse_noe_page(html)
    # print(parse_noe_page(html))
    for item in parse_noe_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(1, 20):
        main(str(i))
        time.sleep(1)
