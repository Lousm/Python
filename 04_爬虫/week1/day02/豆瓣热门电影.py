import requests, re, json


# 请求网页，返回响应体
def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    }
    req = requests.get(url, headers=headers)

    html = req.text
    print(html)
    html = re.sub('\\\\', '', html)#去掉文本中的\\
    if req.status_code == 200:
        return html
    return None


def parse_page(html):
    pattent = re.compile('rate":"(.*?)".*?title":"(.*?)".*?url":".*?(.*?)"')
    content = re.findall(pattent, html)
    for i in content:
        yield {
            '评分': i[0],
            '电影名称': i[1],
            '链接地址': i[2],
        }

# 将结果写入到文件
def write_to_file(content):
    with open('豆瓣热门电影.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')



def main(num):
    url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start='+num
    html = get_page(url)
    print(html)
    print(num)
    content = parse_page(html)
    for item in content:
        print(item)
        write_to_file(item)
    # print(content)


if __name__ == '__main__':
    for i in range(14):
        main(str(i*20))
