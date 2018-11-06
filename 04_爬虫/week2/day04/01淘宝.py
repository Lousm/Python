import requests, pymongo, json, time
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common import keys


# drive = webdriver.PhantomJS(
#     executable_path=r'C:\Users\Mr_Lou\Desktop\新建文件夹 (2)\phantomjs-2.1.1-windows\bin\phantomjs.exe')


def get_page():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
        'cookie': 'thw=cn; cna=UxZ7E/86wiYCAT2ela1d6q9D; hng=CN%7Czh-CN%7CCNY%7C156; miid=151722901403145867; t=b4754e0bde07fede9039744c3fbf7f98; cookie2=360e564e26129f32713ce738cc4e260f; v=0; _tb_token_=e5db643d3648a; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; _m_h5_tk=ab8d5fa6c2792397f58d3c8f06e93e02_1539868083500; _m_h5_tk_enc=197d759472b3894490b077c0f603bd02; unb=1750645818; sg=98b; _l_g_=Ug%3D%3D; skt=d75d3368493fe070; cookie1=BxT%2BigJR3BhllmJvEswq6T48o%2FDzo9ieDKM4LrQAlMQ%3D; csg=9a21ca91; uc3=vt3=F8dByRmr2dXSxcvZhp0%3D&id2=UoYby3Lv6xsWow%3D%3D&nk2=F5RMGyZcnFTj7A%3D%3D&lg2=UIHiLt3xD8xYTw%3D%3D; existShop=MTUzOTg2MDk2OA%3D%3D; tracknick=tb92549359; lgc=tb92549359; _cc_=W5iHLLyFfA%3D%3D; dnk=tb92549359; _nk_=tb92549359; cookie17=UoYby3Lv6xsWow%3D%3D; tg=0; enc=1o3IX9JDEkVSdnvVegrgsKQPaju7FoHNM6%2F153%2BNKdZ7hk3qbqllCrb%2FbWjUO2nyBCs4BfFfbFsAJzLkplc7LQ%3D%3D; birthday_displayed=1; mt=ci=53_1; swfstore=168051; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; uc1=cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&cookie21=VFC%2FuZ9ajC0X15Rzt0LhxQ%3D%3D&cookie15=WqG3DMC9VAQiUQ%3D%3D&existShop=false&pas=0&cookie14=UoTfItjVbQQQaw%3D%3D&tag=8&lng=zh_CN; whl=-1%260%260%261539865581240; _uab_collina=153986558222141590985405; _umdata=0823A424438F76AB59797D9364602E677410264A3C1F7300F23EE805AF82C25C09466624EE67BB7ACD43AD3E795C914C85E8219E7F8BAC4B799257F8402E323D; x5sec=7b227365617263686170703b32223a22343563613836306332383330393539633331303732306332646434326234623543504c336f6434464549376831347a30754a366877414561444445334e5441324e4455344d5467374d513d3d227d; isg=BN7ebYV_CcEYeVwZkxm9qgWFL3Qqlfm90kxM_4hmSCBWq3-F8C6bKW4Jp_cCk5ox; JSESSIONID=4AD035052F1C4BA187514204C7BCA3EF'
                  + 'referer: https://s.taobao.com/search/_____tmd_____/verify/?nc_token=2da4075b29b0cfeaeffd7970b5f7ed57&nc_session_id=01evgjNPL_YJ-uHoaOyfLRrZBV4ZfS-GEomg2TkLlYyKXVXH06g6y6S1pneWbSlLEaBxcs32Y5e1eT-bTbWY6pTvre77vaHA_IicJzsuhvY1bg-UF1MwiQJDLVemkJuQIg&nc_sig=051xMxlkTj9R91rNBaX-utVbrcIWqSNM2AmCEmtPWiiwpnSWQh1Exayk-r3jTxExL7mpXYlQu9q8rXwJHKqDOiLoEQvOToaSCXh0MAqcZQVa-IFdEY0bkxEVxPix3q1HapNDkEASeqU2YJ5Vi1AUsx1sf9fLNdnMj_FeZ5Ryj5YTiTiPKocJOdnXfWKeshLeyA5dWbVY1JTe_o630IVsEq6pjE0TeSIQtIcAhcqzUD9QtqAaCzBCuxdVAwn3naKPLW8IGuli5xsL4vh0d1Jkgnzt2XQM3VuGGMMnMKJEtlvVT66kqfWDZ8gA3XCryYtxVG&x5secdata=5e0c8e1365474455070961b803bd560607b52cabf5960afff39b64ce58073f78f68ede033dd239842063c29628191423866f9620b863c667132a90ce579d5cd7827c2d9284a0516eb74823ad4b449a7d4f0528c27de0a852fbb958e3eaca6e2345cb0ce36cef9f62cbd52852a03cf8ba461ee819ca12264cfd380e1ff9a31817a9305d1c368b15beeed8ff3608c779b3c694396b8f53bc040fe85d7f7c59b17e0761a529de6053c039845272fefc06b979a52a883b8d79c21b1904b01749f64ff68ede033dd239842063c29628191423f26a33fc19185ca7f5ba435d1801cd576b8357c40b8852e10bee2dd322fdfa01b85d13ca384528f05b373d3a77a70575ad921bb1d36afdc5973c0455682491a957f7918a4f2572499cc398910575bb4ae5b2a48d9c0185c8d8521d59b4860b926eb017c803a2fdfc6b9d949ee54258744440bf0b3e57db00024c36b841c1cc35ed81c65bebf3b9df46dd6afed6f199892c38573d94a1e033206e485398b2371f6578a595e91f44da415c8660f5f2584e59ff026c9b1ccc6bbe786d63e6afc08bf9cc5f7bf0afd11a11abde137614009c3edf270ab829c737b0e96e1c97577c93422e5711b423a4c5b28300d059b9c9c4ea96ac905a698405cefae4cfc8bc5c3c5ae3c844d054f41cc5c1e3adeb3f6576b28544a8e0251b3898b48e57b56bef6a977bb3723d732be530f72860a11eb01aed31ec86b3d098df45dd6167eb511a0668841e4294780f577b6f26db88c237492c29707c1857286e8b6c84f82afc633a&x5step=100'
    }
    url = 'https://s.taobao.com/search?ie=utf8&initiative_id=staobaoz_20181018&stats_click=search_radio_all%3A1&js=1&imgfile=&q=%E7%99%BD%E9%85%92&suggest=0_1&_input_charset=utf-8&wq=baijiu&suggest_query=baijiu&source=suggest'
    # url = 'https://s.taobao.com/api?_ksTS=1539862057811_280&callback=jsonp281&ajax=true&m=customized&stats_click=search_radio_all:1&_input_charset=utf-8&bcoffset=-1&js=1&suggest=0_1&source=suggest&suggest_query=baijiu&q=%E7%99%BD%E9%85%92&s=36&initiative_id=staobaoz_20181018&imgfile=&wq=baijiu&ie=utf8&rn=e87f48d89f54cbe48dc27c55ddfee968'
    data = {
        'ie': 'utf8',
        'initiative_id': 'staobaoz_20181018',
        'stats_click': 'search_radio_all:1',
        'js': '1',
        'imgfile': '',
        'q': '白酒',
        'suggest': '0_1',
        '_input_charset': 'utf - 8',
        'wq': 'baijiu',
        'suggest_query': 'baijiu',
        'source': 'suggest'
    }

    con = requests.get(url=url, headers=headers).content.decode('utf-8')

    print(con)
    # new_con = con[11:-2]
    # data = json.loads(new_con)
    # print(type(data))
    # print(data)
    # print(data['API.CustomizedApi'])
    # print(data['API.CustomizedApi']['itemlist'])
    # print(data['API.CustomizedApi']['itemlist']['auctions'])
    # for i in data['API.CustomizedApi']['itemlist']['auctions']:
    #     print(i['title'])


def get_data():
    url = 'https://s.taobao.com/search?ie=utf8&initiative_id=staobaoz_20181018&stats_click=search_radio_all%3A1&js=1&imgfile=&q=%E7%99%BD%E9%85%92&suggest=0_1&_input_charset=utf-8&wq=baijiu&suggest_query=baijiu&source=suggest&bcoffset=6&ntoffset=6&p4ppushleft=1%2C48&s=0'
    drive.get(url)
    print(drive.page_source)

    with open('taobao.html', 'w', encoding='utf-8')as f:
        f.write(drive.page_source)

    # 获得验证码图片 扫码登录
    tree = etree.HTML(drive.page_source)
    src = 'http:' + tree.xpath('.//div[@id="J_QRCodeImg"]/img/@src')[0]
    tu = requests.get(src).content
    # 保存二维码
    with open('二维码.png', 'wb')as f:
        f.write(tu)

    input()
    time.sleep(10)
    drive.save_screenshot('taobai01.png')
    print(src)
    drive.find_element_by_id('q').send_keys('白酒')
    drive.find_element_by_class_name('submit icon-btn-search').click()
    time.sleep(5)

    drive.save_screenshot('taobao02.png')


if __name__ == '__main__':
    get_page()
    # get_data()
