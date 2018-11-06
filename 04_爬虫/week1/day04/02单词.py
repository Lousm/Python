import requests
from lxml import etree


def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content.decode('utf-8')
    return None


def parse_page(con):
    tree = etree.HTML(con)
    tr_list = tree.xpath('//table[@class="table table-bordered table-striped"]//tr')
    for tr in tr_list:
        y = tr.xpath('.//strong/text()')
        h = tr.xpath('.//td[2]/text()')
        a = y[0] + ':' + h[0]
        with open('单词.txt', 'a', encoding='utf-8') as f:
            f.write(a)


def main(page):
    url = 'https://www.shanbay.com/wordlist//110521/232414/?page=' + page
    con = get_page(url)
    parse_page(con)


if __name__ == '__main__':
    for i in range(1, 4):
        main(str(i))
