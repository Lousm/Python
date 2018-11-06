from selenium import webdriver
from lxml import etree
from openpyxl import workbook

def error(list):
    if len(list)==0:
        return 0
    else:
        return list[0].strip()

def get_data(ws, con):
    tree = etree.HTML(con)
    li_list = tree.xpath('.//ul[@id="live-list-contentbox"]/li')

    for li in li_list:
        name = error(li.xpath('.//h3[@class="ellipsis"]/text()'))
        # print(name)
        tag = error(li.xpath('.//span[@class="tag ellipsis"]/text()'))
        zhubo = error(li.xpath('.//span[@class="dy-name ellipsis fl"]/text()'))
        hot = error(li.xpath('.//span[@class="dy-num fr"]/text()'))
        ws.append([name, tag, zhubo, hot])


def main():
    wb = workbook.Workbook()
    ws = wb.active
    ws.append(['房间', '分类', '主播', '热度'])

    drive = webdriver.PhantomJS(
        executable_path=r'C:\Users\Mr_Lou\Desktop\新建文件夹 (2)\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    url = 'https://www.douyu.com/directory/all'
    drive.get(url)
    get_data(ws, drive.page_source)

    page = 1
    while True:
        if 'shark-pager-next shark-pager-disable shark-pager-disable-next' in drive.page_source:
            break

        drive.find_element_by_class_name('shark-pager-next').click()

        get_data(ws, drive.page_source)
        page += 1
        print('爬取到第%d页' % page)
    wb.save('斗鱼直播.xlsx')


if __name__ == '__main__':

    main()

