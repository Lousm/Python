# 构建基于wine_quality数据集的回归模型：
'''
注： 葡萄酒的评分在1~10之间，构建线性回归模型，训练wine_quality数据集的训练集数据，训练完后完成测试集的葡萄评分。
（1）合理将数据集拆分为测试集与训练集；
（2）结合真实的评分，给出评价模型的标准值，以及对比图；
（3）详细说明整个算法构建过程；给出自己的见解
'''

import pandas as pd
from pandas import Series, DataFrame
import numpy as np
from sklearn.linear_model import LinearRegression  # 线性回归
from sklearn.metrics import mean_squared_error
import matplotlib as mpl
import matplotlib.pyplot as plt


# 读取数据
def read_data(data_path=""):
    test_data = pd.read_csv(data_path + "winequality.csv", header=None)
    train_data = pd.read_csv(data_path + "winequality.csv", header=None)
    return train_data, test_data


# 数据处理
def deal_data(pd_data):
    # 获取数据的行数,因为要出去字段名，所以要-1
    row_cnt = pd_data.shape[0] - 1
    # 计算列数，因为在读入数据时，没有指定分隔符，所以所有列数据都是作为一列数据来读入的，因此在计算列数时，将读入的每一行按照;来分开
    column_cnt = len(pd_data.iloc[0, 0].split(";"))
    # empty 会创建一个没有使用特定值来初始化的数组。给这些方法传递一个元组作为形状来创建高维数组：
    X = np.empty((row_cnt, column_cnt - 1))
    Y = np.empty((row_cnt, 1))
    column_name = pd_data.iloc[0, 0].split(";")
    # 开始获取数据
    for i in range(0, row_cnt):
        # 逐一将每一行进行分割（按;空格分割）
        row_array = pd_data.iloc[i + 1, 0].split(";")
        # x取前13个数据，X[i]是一个一维数组，则X相当于一个二维数组，Y同理
        X[i] = np.array(row_array[0:-1])
        # y取最后一个数据
        Y[i] = np.array(row_array[-1])
    return X, Y, column_name


# 把特征标准化为均匀分布
def uniform_norm(X):
    X_max = X.max(axis=0)
    X_min = X.min(axis=0)
    return (X - X_min) / (X_max - X_min), X_max, X_min


# 实现线性回归
# 画图
def draw(pred, test_Y):
    t = np.arange(len(pred))

    # 解决中文不显示
    plt.rcParams['font.sans-serif'] = 'SimHei'
    plt.rcParams['axes.unicode_minus'] = False
    p = plt.figure(facecolor='w')
    p.add_subplot(2, 1, 1)
    plt.plot(t, test_Y, 'r-', lw=2, label='真实数据')
    p.add_subplot(2, 1, 2)
    plt.plot(t, pred, 'b-', lw=2, label='预估值')
    plt.legend(loc='best')
    plt.title('水质', fontsize=18)
    plt.xlabel('case id', fontsize=15)
    plt.ylabel('质量', fontsize=15)
    plt.grid()
    plt.show()


# 模型评估
def evaluate(unif_train_X, train_Y, unif_test_X, test_Y):
    print("训练集上效果评估:")
    pred_train = model.predict(unif_train_X)
    print("R^2系数 ", model.score(unif_train_X, train_Y))
    print("均方误差 ", mean_squared_error(train_Y, pred_train))
    print("\n测试集上效果评估 :")
    r2 = model.score(unif_test_X, test_Y)
    print("R^2系数 ", r2)
    pred = model.predict(unif_test_X)
    print("均方误差 ", mean_squared_error(test_Y, pred))


# 主函数
if __name__ == "__main__":
    # 读取数据
    train_data, test_data = read_data()
    # 数据处理
    train_X, train_Y, column_name = deal_data(train_data)
    # print(train_X.shape)
    # print(train_Y.shape)
    test_X, test_Y, column_name = deal_data(test_data)
    # print(test_X.shape)
    # print(test_Y.shape)
    # 把特征标准化为均匀分布
    unif_train_X, max_X, min_X = uniform_norm(train_X)
    unif_test_X = (test_X - min_X) / (max_X - min_X)
    # 实现线性回归
    model = LinearRegression()
    model.fit(unif_train_X, train_Y)
    # 在训练集上预测
    pred_train = model.predict(unif_train_X)
    # 在测试集上预测
    pred = model.predict(unif_test_X)
    # 画图
    draw(pred, test_Y)
    # 模型评估
    evaluate(unif_train_X, train_Y, unif_test_X, test_Y)
