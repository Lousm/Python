import requests, re, random, time, threading


def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    }
    proxies = {
        'https': '123.132.232.254:37638',
        'https': '119.1.97.193:60916'
    }
    res = requests.get(url=url, headers=headers, proxies=proxies)
    print(res)

    return res.text.encode('ISO-8859-1').decode(res.apparent_encoding, 'ignore')


def parse_page(html):
    pattren = re.compile('class="item_t".*?class="img".*?target="_blank".*?href="(.*?).html".*?<b>(.*?)</b>', re.S)
    all_con = re.findall(pattren, html)
    return all_con


def parse_small_page(small_html):
    pattren = re.compile('id="picnum".*?class="totalpage">(.*?)</span>.*?id="big-pic".*?alt="(.*?)".*?src="(.*?)"',
                         re.S)

    try:
        small_com = re.findall(pattren, small_html)
        return small_com
    except:
        print('404  找不到莫慌')
        return 1


def get_img(url, name):
    num = str(int(time.time() * 10000))[9:] + str(random.randint(1, 1000))
    print(num)
    res = requests.get(url)
    with open('./唯一图库/%s%s.png' % (name, num), 'wb') as f:
        f.write(res.content)
    return


def get_small_page(all_con):
    for i in all_con:
        print(i)
        small_html = get_page(i[0] + '.html')
        small_com = parse_small_page(small_html)
        if small_com!=1:
            for j in small_com:
                print(j)
                for k in range(1, int(j[0]) + 1):
                    if k == 1:
                        a_small_url = i[0] + '.html'
                    else:
                        a_small_url = i[0] + "_" + str(k) + '.html'
                    print(a_small_url)
                    a_small_html = get_page(a_small_url)
                    a_small_com = parse_small_page(a_small_html)
                    if a_small_com!=1:
                        # print(a_small_com)
                        for z in a_small_com:
                            print('zzzzzz')
                            print(z)
                            get_img(z[2], z[1])
                            # a_small_com = parse_small_page(small_html)


def start_a(page):
    if page == 1:
        url = 'http://www.mmonly.cc/tag/mmz/index.html'
    else:
        url = 'http://www.mmonly.cc/tag/mmz/' + str(page) + '.html'
    url
    print(url)
    html = get_page(url)
    all_con = parse_page(html)
    get_small_page(all_con)


def main():
    for i in range(1, 10):
        t = threading.Thread(target=start_a, args=(str(i),))
        t.start()


if __name__ == '__main__':
    main()
