import requests, json
from lxml import etree


def get_page(data):
    url = 'https://www.creditchina.gov.cn/api/credit_info_search'
    # print(data)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    }
    con = requests.get(url=url, headers=headers, params=data).content.decode('utf-8')
    return con


def main():
    for i in range(1, 11):
        data = {
            'keyword': '中公教育',
            'templateId': '',
            'page': str(i),
            'pageSize': '10'
        }
        con = json.loads(get_page(data))
        print('page'+str(i))
        dic = con["data"]['results']
        for j in dic:

            st = '公司名称： ' + j['name'] + '  工商注册号: ' + j['idCardOrOrgCode']
            print(st)


if __name__ == '__main__':
    main()
