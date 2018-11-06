from selenium import webdriver
import json, threading
from lxml import etree

drive = webdriver.PhantomJS(
    executable_path=r'C:\Users\Mr_Lou\Desktop\新建文件夹 (2)\phantomjs-2.1.1-windows\bin\phantomjs.exe')


def get_data(page):
    url = 'http://www.stat-nba.com/query.php?page=' + str(
        page) + '&QueryType=all&AllType=season&AT=avg&order=1&crtcol=pts&PageNum=60#label_show_result'
    drive.get(url)

    tree = etree.HTML(drive.page_source)

    tr_list = tree.xpath('//tbody')
    print(tr_list)

    for tr in tr_list:
        name = tr.xpath('.//td[2]//text()')
        # print(name)
        tim = tr.xpath('.//td[5]/text()')
        lanban = tr.xpath('.//td[15]/text()')
        zhugong = tr.xpath('.//td[18]/text()')
        deifen = tr.xpath('.//td[23]/text()')
        for j in range(60):
            item = {}
            item['球员'] = name[j]
            item['时间'] = tim[j]
            item['篮板'] = lanban[j]
            item['助攻'] = zhugong[j]
            item['得分'] = deifen[j]

            data = json.dumps(item, ensure_ascii=False)
            with open('NBA数据爬取.json', 'a', encoding='utf-8')as f:
                f.write(data + '\n')


def main():
    for page in range(10):
        t = threading.Thread(target=get_data, args=(page,))
        t.start()


if __name__ == '__main__':
    main()
