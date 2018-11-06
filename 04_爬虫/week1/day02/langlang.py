from urllib import request, parse
import ssl, re

ssl._create_default_https_context = ssl._create_stdlib_context


def get_img(num):
    url = 'http://langlang2017.com/img/banner%s.png' % num
    res = request.urlopen(url).read()
    print(res)

    # with open('banner%s.png' % num, 'wb') as f:
    #     f.write(res)


if __name__ == '__main__':
    for i in range(1, 5):
        get_img(str(i))
