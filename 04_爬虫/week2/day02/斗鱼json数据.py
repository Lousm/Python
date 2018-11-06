import requests, json, time
from openpyxl import workbook
import warnings
from multiprocessing.dummy import Pool

warnings.filterwarnings("ignore")

wb = workbook.Workbook()
ws = wb.active
ws.append(['房间', '热度', '主播', '分类'])


def get_data(page, start=0):
    url = 'https://www.douyu.com/gapi/rkc/directory/0_0/' + page
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    }

    con = requests.get(url=url, headers=headers, verify=False).content.decode('utf-8')
    # print(type(con))
    # print(con)
    dick = json.loads(con)
    if start == 1:
        return int(dick['data']['pgcnt'])

    for i in dick['data']['rl']:
        name = i['rn']
        hot = i['ol']
        zhubo = i['nn']
        fenlei = i['c2name']
        ws.append([name, hot, zhubo, fenlei])
    # print('第%s页爬取完成' % page)
    return 1


# 单线程
# def main():
#     page_num = get_page_num()
#     for page in range(1, page_num + 1):
#         get_data(str(page))
#         print('第%d页爬取完成' % page)
#     wb.save('斗鱼直播json数据.xlsx')

# 多线程
def main(pool):
    page_num = get_data(str(1), 1)  # 获取总共有多少页
    pa_start_time = time.time()

    # 开启多线程

    p = Pool(pool)
    page_list = []
    for page in range(1, page_num + 1):
        page_list.append(str(page))
    p.map(get_data, page_list)
    p.close()
    p.join()

    pa_time = time.time() - pa_start_time
    print('共%d页' % page_num)
    f.write('共%d页' % page_num + '\n')

    print('爬取数据用时 %2f' % pa_time)
    f.write('爬取数据用时 %2f' % pa_time + '\n')

    cun_start_time = time.time()
    wb.save('斗鱼直播json数据(线程池大小%d).xlsx' % pool)
    cun_time = time.time() - cun_start_time
    print('存储数据用时 %2f' % cun_time)
    f.write('存储数据用时 %2f' % cun_time + '\n')

    print('总共用时 %2f' % (pa_time + cun_time))
    f.write('总共用时 %2f' % (pa_time + cun_time) + '\n')

    print('线程池大小 %d' % pool)
    print()
    f.write('线程池大小 %d' % pool + '\n')
    f.write('\n')


if __name__ == '__main__':
    f = open('线程池大小与时间开销对比.txt', 'a', encoding='utf-8')
    for pool in range(20, 31):
        main(pool)
    f.close()
