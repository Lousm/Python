import numpy as np
import pandas as pd
import operator
from collections import Counter


def get_data():
    movie = pd.read_excel('电影分类数据.xlsx')
    # 样本属性
    shuxing = list(movie.iloc[:, 2:5].values)
    a = []

    # 样本标签
    labels = str(movie.iloc[:, 5:6].T.values)[2:-2].split(' ')
    b = []

    # 测试数据
    ceshi = list(movie.iloc[:0, 7:12])
    for i in shuxing:
        a1 = []
        st = str(i)[1:-1].split(' ')
        for j in st:
            if j != '':
                a1.append(int(j))
        a.append(a1)

    for i in labels:
        b.append(i[1:-1])
    return a, b, ceshi


def odistance(shuxing, labels, ceshi, k):
    for i in range(len(shuxing)):
        distance = np.sqrt(np.square(shuxing[i][0] - ceshi[0]) + np.square(shuxing[i][1] - ceshi[1]) + np.square(
            shuxing[i][2] - ceshi[2]))
        distance_lis.update({distance: labels[i]})
    after = sorted(distance_lis.items(), key=operator.itemgetter(0))

    lis = list(dict(after).values())
    lis_ = []

    for i in range(k):
        lis_.append(lis[i])
    print('测试数据为：', ceshi)
    print('分类结果为：', Counter(lis_).most_common(1))


if __name__ == '__main__':
    distance_lis = {}
    shuxing, labels, ceshi = get_data()
    odistance(shuxing, labels, ceshi, 5)
