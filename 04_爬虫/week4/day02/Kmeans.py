import pandas as pd
import numpy as np
import heapq
import matplotlib.pyplot as plt

order = pd.read_csv('company.csv', sep=',', encoding='gbk')

price = order['平均每次消费金额'].values.tolist()
day = order['平均消费周期（天）'].values.tolist()
print(price)
print(day)


# 中心到各个节点的距离
def get_distance(x1, y1, x2, y2):
    return np.sqrt(np.power((x1 - x2), 2) + np.power((y1 - y2), 2))


# 第一次得到随机中心节点
def get_base_list(k):
    base_lis = np.random.randint(0, len(price), k)
    for i in base_lis:
        a = []
        a.append(day[i])
        a.append(price[i])
        center_lis.append(a)
    return base_lis


#
def get_center(lis):
    sumx = 0
    sumy = 0
    a = []
    for i in lis:
        sumx += i[0]
        sumy += i[1]
    a.append(sumx / len(lis))
    a.append(sumy / len(lis))
    center_lis.append(a)


# 各个中心点包含的点
def get_centreOfevery(lis_):
    cent = {}

    # 各个点到中心点的距离
    lis = {}
    for j in range(len(day)):
        distance_lis = []
        dian_xy = []
        dian_xy.append(day[j])
        dian_xy.append(price[j])
        for i in lis_:
            if i[0] != day[j] and i[1] != price[j]:
                distance = get_distance(i[0], i[1], day[j], price[j])
                distance_lis.append(distance)
        lis.update({tuple(dian_xy): distance_lis})

    for i in center_lis:
        b = []
        for key, value in lis.items():
            min_n = 1
            temp = map(value.index, heapq.nsmallest(min_n, value))
            temp = list(temp)
            if center_lis[temp[0]] == i:
                b.append(list(key))
            # print(key, '属于', center_lis[temp[0]])
        cent.update({tuple(i): b})
    return cent


if __name__ == '__main__':
    # 中心点
    center_lis = []
    base_lis = get_base_list(4)
    print(base_lis)

    b = []
    for i in base_lis:
        a = []
        a.append(day[i])
        a.append(price[i])
        b.append(a)
    cent = get_centreOfevery(b)

    print('中心点:')
    print(center_lis)

    while True:
        a1 = center_lis[0][0]
        b1 = center_lis[1][0]
        c1 = center_lis[2][0]
        center_lis.clear()
        for key, value in cent.items():
            get_center(value)
        print('中心点：')
        print(center_lis)

        cent = get_centreOfevery(center_lis)
        print('各个中心点包含的点：')
        print(cent)
        print('-' * 50)
        if a1 == center_lis[0][0] and b1 == center_lis[1][0] and c1 == center_lis[2][0]:
            break

    # 解决中文不显示
    plt.rcParams['font.sans-serif'] = 'SimHei'
    plt.rcParams['axes.unicode_minus'] = False

    p = plt.figure(figsize=(10, 10), dpi=80)
    p.add_subplot(1, 2, 1)
    plt.scatter(day, price, marker='o', color='g')

    centx = []
    centy = []
    for i in center_lis:
        centx.append(i[0])
        centy.append(i[1])

    p.add_subplot(1, 2, 2)
    plt.scatter(centx, centy, marker='*', color='r')

    for key, value in cent.items():
        x = []
        y = []
        for i in value:
            x.append(i[0])
            y.append(i[1])
        plt.scatter(x, y, marker='o')

    plt.show()
