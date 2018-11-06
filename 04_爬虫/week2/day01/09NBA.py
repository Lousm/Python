from bs4 import BeautifulSoup
import threading, requests, time
from openpyxl import workbook


def get_data(ws, page):
    url = 'http://www.stat-nba.com/query.php?page=' + str(
        page) + '&QueryType=all&AllType=season&AT=avg&order=1&crtcol=pts&PageNum=60#label_show_result'
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    }
    con = requests.get(url=url, headers=headers).content
    soup = BeautifulSoup(con, 'lxml')

    tr_list = soup.select('tbody > tr')

    for tr in tr_list:
        name = tr.select('td')[1].get_text()
        tim = tr.select('td')[4].get_text()
        lanban = tr.select('td')[14].get_text()
        zhugong = tr.select('td')[17].get_text()
        defen = tr.select('td')[22].get_text()

        ws.append([name, tim, lanban, zhugong, defen])


def main():
    wb = workbook.Workbook()
    ws = wb.active

    ws.append(['球员', '时间', '篮板', '助攻', '得分'])
    for i in range(72):
        t = threading.Thread(target=get_data, args=(ws, i))
        t.start()
        time.sleep(0.1)
        t.join()
    wb.save('NBA球员信息.xlsx')


if __name__ == '__main__':
    main()
