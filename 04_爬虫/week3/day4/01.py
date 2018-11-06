import pandas as pd
import numpy

order = pd.read_csv('meal_order_info.csv', sep=',', encoding='gbk')
# print(order)

# pd.read_table()
# order.to_csv('文件名.csv', sep=',', index=False)
# index代表 狮吼剑行明写出（索引），默认为True

user = pd.read_excel('users.xlsx')
detail = pd.read_excel('meal_order_detail.xlsx')
# print(detail)

# 存储文件
# user.to_excel('user.xlsx')

# DataFeame的常用属性
# values  columns  dtypes
# print(user.values)
# print(user.columns)
# print(user.dtypes)

# print(user.shape)
# print(user.size)
# print(user.ndim)

# print(order.T.shape)
# print(order.index)

###########增删查改############DataFrame

# 取dishes_name列 的前5个
# print(detail['dishes_name'][:4])

# 如果要查找多列 则传入一个列表
# print(detail[['dishes_name','order_id']][:4])

# 查找所有列的 2:5行
# print(detail[:][1:6])

# 读取前5行
# print(detail.head())
# 读取后5行
# print(detail.tail())

# loc 方法是针对 DataFrame 索引名称的切片方法，如果传入的不是索引名称，那么切片
# 操作将无法执行。

# iloc 方法的使用方法如下。
# DataFrame.iloc[行索引位置, 列索引位置]

# print(detail.loc[:, 'dishes_name'])
# print(detail.iloc[:, 2])

# 多列切片
# print(detail.loc[:, ['order_id', 'dishes_name']])
# print(detail.iloc[:, [2, 5]])

# 条件切片
# detail['order_id']==458 给定行的条件
# print(detail.loc[detail['order_id'] == 458, ['order_di', 'dishes_name']])
# print(detail.iloc[(detail['order_id'] == 458).values, [1,5]])

# 更改
# 将order_id=458的值改为45800
# detail.loc[detail['order_id'] == 458, 'order_id'] = 45800
# print(detail.loc[detail['order_id'] == 45800, ['order_di', 'dishes_name']])

##填数据 （增加一列）
# detail['payment'] = detail['counts'] * detail['amounts']
#
# detail['payway'] = '现金支付'
# print(detail)

# drop删除
# inplace 是否对原表生效，默认False
# labels 删除的行或列的标签

# s删除1列
# detail.drop(labels='payway',axis=1,inplace=True)
# print(detail.columns)

# 删除行
# print(len(detail))
# detail.drop(labels=range(1,11),axis=0,inplace=True)
# print(len(detail))

# 统计函数
# describe describe，能够一次性得出数据框所有数值型特征的非空 值数目、均值、四分位数、标准差
# describe 方法除了支持传统数值型以外，还能够支持对 category 类型的数据进行描述性
# 统计，四个统计量分别为列非空元素的数目，类别的数目，数目最多的类别，数目最多
# 类别的数目

# detail[:] = detail[:].astype('category')
# print(detail[:].describe())

# a = detail.columns
# b = list(a)
# print(detail.isnull())
#
# for i in b:
#     # print(detail[i].isnull()[-1:])
#     # print(type(detail[i].isnull()))
#
#     if detail[i].isnull()[-1:][:, 1] == False:
#         detail.drop(labels=i, axis=1, inplace=True)
#
# print(detail.shape)


##################提取时间
# week
# quar
# weekday 一周的第几天

# 转换为标准时间
order['user_time'] = pd.to_datetime(order['use_start_time'])

# print(order['user_time'])
# print(pd.Timestamp.min)
# print(pd.Timestamp.max)

# 提取year
# year = [i.year for i in order['user_time']]
# print(year[:5])

# 提取周几
# week_name = [i.weekday_name for i in order['user_time']]
# print(week_name[:5])

# 是否是闰年
# isleap_year = [i.is_leap_year for i in order['user_time']]
# print(isleap_year)


#######时间加减
# weeks/days/hours/minutes/seconds/millisenconds毫秒/microseconds微秒/nanoseconds纳秒

order['lock_time'] = pd.to_datetime(order['lock_time'])
# print(order['lock_time'][:5])
# 时间加一天
# order['lock_time'] += pd.Timedelta(days=1)
# print(order['lock_time'][:5])

# 时间差
# time1 = order['lock_time'] - pd.to_datetime('2017-1-1')
# print(time1)

# 每个客服用餐时间
# 30天内最早的下单时间 和最晚的下单时间 差值
# 每天的平均营业时间

# 1
# each_time = order['lock_time'] - order['user_time']
# print(each_time[:5])

# 分组统计1 传入分组字段
a = detail[['order_id', 'counts', 'amounts']].groupby(by='order_id')
# print(a.sum()[:5])

# 分组统计2  传入统计函数(队列表进行全部函数统计)
a2 = detail[['order_id', 'counts', 'amounts']].agg([numpy.mean, numpy.sum])
# print(a2[:5])

# 队列表分别进行对应的函数统计
a3 = detail.agg({'counts': numpy.sum, 'amounts': numpy.mean})
a4 = detail.agg({'counts': numpy.sum, 'amounts': [numpy.mean, numpy.std]})
# print(a3[:5])
# print(a4[:5])

# 分组统计3  transform(func)
a5 = detail[['counts', 'amounts']].transform(lambda x: x * 2)
# print(a5[:5])


######创建透视表，交叉表#######
# 默认给的是求均值 mean  这里设置为sum
a6 = pd.pivot_table(detail[['order_id', 'counts', 'amounts']], index='order_id', aggfunc=numpy.sum)
# print(a6)

# pivot_table分组可以设多个

# 指定菜品名做为分组的透视表
a7 = pd.pivot_table(detail[['order_id', 'dishes_name', 'counts', 'amounts']], index=['order_id'], columns='dishes_name',
                    aggfunc=numpy.sum)

# print(a7)
# 用value显示想要的数据
a8 = pd.pivot_table(detail[['order_id', 'dishes_name', 'counts', 'amounts']], index='order_id',
                    aggfunc=numpy.sum, values='counts')
# print(a8)

# 当表中的数据不存在时，用NAN填充
# 可以指定fill_value表示当填充缺失值时，已指定的参数进行填充
a9 = pd.pivot_table(detail[['order_id', 'dishes_name', 'counts', 'amounts']], index='order_id', columns='dishes_name',
                    fill_value=0,
                    aggfunc=numpy.sum, values='counts')
# print(a9)

###############交叉表##################
# crosstab
crosstab = pd.crosstab(index=detail['order_id'], columns=detail['dishes_name'], values=detail['counts'],
                       aggfunc=numpy.sum)
# print(crosstab)

###交叉表也是透视表的一种，crosstab参数和pivot_table函数基本相同。不同之处在于：对于crosstab函数中的index,columns,values
# 输入的都是直接从Dataframe中取出的某一列

########################任务：创建单日菜品成交总数 和 成交总额透视表：##############################################
##创建一个日期列：
detail['place_order_time'] = pd.to_datetime(detail['place_order_time'])
detail['date'] = [i.date() for i in detail['place_order_time']]

##创建一个计算总价后的列：
detail['price'] = detail['counts'] * detail['amounts']
##创建透视表：以date作为行索引，分别求price/counts的sum；
dishes_pivot_table = pd.pivot_table(detail[['date', 'price', 'counts']], index='date', aggfunc=numpy.sum)
# print(dishes_pivot_table)
##############################################################################################################
dict1 = {'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9],
         'System': ['win10', 'win10', numpy.nan, 'win10', numpy.nan, numpy.nan, 'win7', 'win7', 'win8'],
         'cpu': ['i7', 'i5', numpy.nan, 'i7', numpy.nan, numpy.nan, 'i5', 'i5', 'i3']}
dict2 = {'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9],
         'System': [numpy.nan, numpy.nan, 'win7', numpy.nan, 'win8', 'win7', numpy.nan, numpy.nan, numpy.nan],
         'cpu': [numpy.nan, numpy.nan, 'i3', numpy.nan, 'i7', 'i5', numpy.nan, numpy.nan, numpy.nan]}
df1 = pd.DataFrame(dict1)
# print(df1.shape)
df2 = pd.DataFrame(dict2)
# print(df2.shape)

##############数据清洗###################
# 1检测与处理重复数据  两种
# 一 记录重复，即一个或多个特征的某几条记录完全相同
# 二一个或多个特征名不同，数据完全相同
# 用  drop_duplicates() 方法

##############两列去重：在同一行上的这两个值相同，则判断为重复


# 相似度计算,取特征值
# Kendall  spearman
# 只针对数值型的数据，如果参数包含其它类型 则不比较这个非数值型 如下c2,c4 计算的结果就不包含dishes_name
# kendall：单调相关性；与spearman区别在于某一比较数据需要有序，在有序情况下计算速度比spearman快。
# c1 = detail[['counts', 'amounts']].corr(method='spearman')
# c2 = detail[['counts', 'amounts','dishes_name']].corr(method='spearman')
# c3 = detail[['counts', 'amounts']].corr(method='kendall')
# c4 = detail[['counts', 'amounts','dishes_name']].corr(method='kendall')
# print(c2)
# print(c4)

#######检测处理缺失值
# 对于空值有两种处理的方法，第一种是使用fillna函数对空值进行填充，
# 可以选择填充0值或者其他任意值。第二种方法是使用dropna函数直接将
# 包含空值的数据删除。
# 检测缺失值的数目
# print(detail.isnull().sum())

# 去除缺失值
# print('去除缺失值前的shape', detail.shape)
# print('去除缺失值后的shape', detail.dropna(axis=1, how='any').shape)

from scipy.interpolate import interp1d

x = numpy.array([1, 2, 3, 4, 5, 8, 9, 10])
y1 = numpy.array([2, 8, 18, 32, 50, 128, 162, 200])
y2 = numpy.array([3, 5, 7, 9, 11, 17, 19, 21])

line1 = interp1d(x, y1, kind='linear')
line2 = interp1d(x, y2, kind='linear')

#####3σ原则--拉依达准则

# mi = detail['amounts'].mean - detail['amounts'].std
# ma = detail['amounts'].mean + detail['amounts'].std
# print(mi)
# print(ma)


# 标准化

# （1）离差标准化
# x=x-min/max-min

# （2）均值标准化给予原始数据的均值（mean）和标准差（standard deviation）进行数据的标准化。
# 经过处理的数据符合标准正态分布，即均值为0，标准差为1。转化函数为：

# （3）小数定标标准化
# 假定A的值由-986到917，A的最大绝对值为986，为使用小数定标标准化，我们用每个
# 值除以1000（即，j=3），这样，-986被规范化为-0.986。 （以最大值为标准使这一列的小数点像左移动相应的位数）

# 转换数据
###哑变量处理
##稀疏矩阵
# print(pd.get_dummies((detail['dishes_name'])))

###离散化连续型数据
# 等宽法
price = pd.cut(detail['amounts'], 5)
print(price.value_counts())

# 等频法 离散化函数
