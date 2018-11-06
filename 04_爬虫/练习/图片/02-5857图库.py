import requests, re, json, time, random, threading
from urllib import request


# 请求网页，返回页面
def get_page(url, status):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    print(response)
    if response.status_code == 200:
        # .encode('ISO-8859-1').decode(response.apparent_encoding)
        if status == 0:
            return response.text
        else:
            return response.text.encode('ISO-8859-1').decode(response.apparent_encoding)
    return None


# 分析整体页面
def parse_all_page(all_html, pattern):
    res = re.findall(pattern, all_html)
    return res


# 分析单独页面
def parse_small_page(small_html):
    # print(small_html)
    pa = re.compile('<div.*?class="main".*?<h1.*?class="main_center_h2">(.*?)<span>.*?'
                    + '.*?<div.*?class="main_center_img".*?</a>.*?<img.*?src="(.*?)".*?alt', re.S)
    # pa = re.compile('<div.*?class="main".*?<h1.*?class="main_center_h2">(.*?)<span>.*?</b>/(.*?)</em>', re.S)

    try:
        res = re.findall(pa, small_html)
        return res
    except:
        print('404  找不到莫慌')
        return 1


# 得到整体页面里的连接
def all_link(page):
    # all_url = 'http://www.5857.com/tag_mengmeizi.html'
    # all_url = 'http://www.5857.com/index.php?m=search&c=index&a=init&typeid=3&q=%E6%98%8E%E6%98%9F'
    # all_url = 'http://www.5857.com/html/hotlist-' + page + '.html'
    all_url = 'http://www.5857.com/tag_siwameinv.html'
    print(all_url)

    # 如果有中文乱码就传参数一
    all_html = get_page(all_url, 0)
    # all_html = get_page(all_url, 1)

    # 设置正则
    set_pattern(all_html)


# 生成图片
def get_img(url, name, a):
    num = str(int(time.time() * 10000))[9:] + str(random.randint(1, 1000))
    print(num)
    res = request.urlopen(url)
    with open('./妹子/%s%s.png' % (name, num), 'wb') as f:
        f.write(res.read())
    return


# 设置正则
def set_pattern(all_html):
    # 热门壁纸
    pattern1 = re.compile('<div.*?class="listbox">.*?href="(.*?).html".*?title="(.*?)"'
                          + '.*?<em.*?class="page_num">共(.*?)张', re.S)

    # 明星，萌妹子（搜索框得到的页面）
    pattern2 = re.compile('<div.*?class="listbox">.*?href="(.*?).html".*?color=red>(.*?)</font>'
                          + '.*?<em.*?class="page_num">共(.*?)张', re.S)
    # pa = re.compile('<div.*?class="listbox">.*?href="(.*?)".*?color=red>(.*?)</font>', re.S)

    all_res = parse_all_page(all_html, pattern1)

    get_eventual_link(all_res)


# 得到最底层的连接
def get_eventual_link(all_res):
    # 循环所有连接得到各个页面
    for i in all_res:
        for k in range(1, int(i[2]) + 1):  # 分别访问子页面的每张图片
            if k == 1:
                small_url = i[0] + '.html'
            else:
                small_url = i[0] + '_' + str(k) + '.html'
            print(small_url)
            small_html = get_page(small_url, 1)
            # 调用方法 分离数据
            small_res = parse_small_page(small_html)
            if small_res != 1:
                num = 0
                num += 1
                for j in small_res:
                    get_img(j[1], j[0], num)
                    print(j[0] + j[1])
                # print(i[0] + i[1]+i[2]+i[3])
        print(i[0] + i[1] + i[2])


def main():
    all_link(1)
    # for i in range(1, 40):
    #     t = threading.Thread(target=all_link, args=(str(i),))
    #     t.start()


if __name__ == '__main__':
    main()
