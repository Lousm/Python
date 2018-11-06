from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from lxml import etree
import time
from openpyxl import workbook
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
KEY = '白酒'
url = 'https://www.taobao.com/'
browser.get(url)


def get_one_page():
    wb = workbook.Workbook()
    ws = wb.active
    ws.append(['商品名', '价格', '付款人数', '店铺', '地址'])

    time.sleep(3)

    # # 获取当前窗口句柄（窗口A）(还停留在百度页面（A）)
    # handle = browser.current_window_handle
    # # 获取当前所有窗口句柄（窗口A、B）
    # handles = browser.window_handles
    # # 对窗口进行遍历
    # for newhandle in handles:
    #     # 筛选新打开的窗口B
    #     if newhandle != handle:
    #         # 切换到新打开的窗口B
    #         browser.switch_to_window(newhandle)

    browser.find_element_by_id('q').send_keys(KEY)
    browser.find_element_by_xpath('//button[@class="btn-search tb-bg"]').click()

    con = browser.page_source

    input('输入1继续')
    get_data(ws, con)

    for i in range(100):
        if i == 0:
            down1()
        else:
            down2()

        browser.find_element_by_xpath('//li[@class="item next"]').click()

        time.sleep(5)
        get_data(ws, browser.page_source)
        print('爬取到第%d页' % (i + 2))
    wb.save('淘宝商品--%s.xlsx'%KEY)


def get_data(ws, con):
    tree = etree.HTML(con)
    # print(con)
    goods_list = tree.xpath('.//div[@class="item J_MouserOnverReq  "]')
    # print(goods_list)
    for goods in goods_list:
        a = goods.xpath('.//div[@class="ctx-box J_MouseEneterLeave J_IconMoreNew"]//a[@class="J_ClickStat"]')[0]
        name = a.xpath('string(.)').strip()
        p_data = goods.xpath(
            './/div[@class="ctx-box J_MouseEneterLeave J_IconMoreNew"]//div[@class="price g_price g_price-highlight"]//text()')
        price = p_data[2]
        pnum = goods.xpath(
            './/div[@class="ctx-box J_MouseEneterLeave J_IconMoreNew"]//div[@class="deal-cnt"]/text()')[0]
        shop_name = goods.xpath(
            './/div[@class="ctx-box J_MouseEneterLeave J_IconMoreNew"]//div[@class="row row-3 g-clearfix"]//a/span[last()]/text()')[
            0]
        address = goods.xpath(
            './/div[@class="ctx-box J_MouseEneterLeave J_IconMoreNew"]//div[@class="row row-3 g-clearfix"]/div[@class="location"]/text()')[
            0]
        # print(name+' '+price+' '+pnum+' '+shop_name+' '+address)
        # print(name)
        ws.append([name, price, pnum, shop_name, address])


def down1():
    js = "var q=document.documentElement.scrollTop=1000"
    browser.execute_script(js)
    time.sleep(1)
    js = "var q=document.documentElement.scrollTop=2000"
    browser.execute_script(js)
    time.sleep(1)
    js = "var q=document.documentElement.scrollTop=3000"
    browser.execute_script(js)
    time.sleep(1)
    js = "var q=document.documentElement.scrollTop=4000"
    browser.execute_script(js)
    time.sleep(1)
    js = "var q=document.documentElement.scrollTop=4700"
    browser.execute_script(js)
    time.sleep(1)


def down2():
    js = "var q=document.documentElement.scrollTop=1000"
    browser.execute_script(js)
    time.sleep(1)
    js = "var q=document.documentElement.scrollTop=2000"
    browser.execute_script(js)
    time.sleep(1)
    js = "var q=document.documentElement.scrollTop=3000"
    browser.execute_script(js)
    time.sleep(1)
    js = "var q=document.documentElement.scrollTop=4000"
    browser.execute_script(js)
    time.sleep(1)


if __name__ == '__main__':
    get_one_page()
