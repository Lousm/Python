import numpy
import selenium
from numpy import matlib

# arr1 = numpy.array([1, 2, 3, 4])
# # print(arr1)
#
arr2 = numpy.array(
    [[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11], [2, 5, 6, 8], [1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11],
     [2, 5, 6, 8]])
# print(arr2)
# print(arr1.dtype)
# print(arr2.dtype)
# print(arr1.size)
# print(arr2.size)
#
# print(arr1.shape)
# print(arr2.shape)
#
# # 维度
# print(arr1.ndim)
# print(arr2.ndim)
# print(arr2)

# 更改维度
# arr2.shape = 2, 2, 2, 2, 2
# print(arr2)
# print(arr2.ndim)

# ############################第二中方法##########################
# 左闭右开
# print(numpy.arange(0, 1, 0.001))

# 等差数列
# 起始值，终值，元素个数
# print(numpy.linspace(1, 12, 12))

# 等比
# 起始值，终值，元素个数
# print(numpy.logspace(0, 2, 20))

# zeros全0矩阵
# print(numpy.zeros((2, 3)))

# 全1矩阵
# print(numpy.ones((5, 3)))

# 对角矩阵
# print(numpy.diag([1, 2, 3, 4]))

# 单位矩阵
# print(numpy.eye(4))

# 随机数--------------------------------------
# 0-1之间100个随机数
# print(numpy.random.random(100))

# 10行5列 服从均匀分布
# print(numpy.random.rand(10, 5))

# 10行5列 服从正太分布
# print(numpy.random.randn(10, 5))

# 随机整数2行5列  左闭右开
# print(numpy.random.randint(2, 10, size=[2, 5]))


###############索引访问数组###################
# arr1 = numpy.arange(10)

# 一维索引
# print(arr1[5])

# 切片 取3-4
# print(arr1[3:5])
# 取前5个
# print(arr1[:5])

# 修改数组元素
# arr1[2:4] = 55, 66
# print(arr1)

# 隔一个取一个
# 取所有行arr[:],步长为2arr[::2]
# print(arr1[::2])

####################二维##################
# arr2 = numpy.arange(15)
# print(arr2)
# arr2.shape = 3, 5
# print(arr2)

# 取2行 6-7
# print(arr2[1, 1:3])

# 取2 3 行的第3 4 5列(下标从0开始)
# print(arr2[1:3, 2:6])

# 取第1行的第5个  和第3行的第4个
# print(arr2[[0, 2], [4, 3]])
# print(arr2[[(0, 2), (4, 3)]])

# 取第2行的第0 2 3个  和第3行的第0 2 3个
# print(arr2[1:3, [0, 2, 3]])

print()

# 根据bool值  取第3行的值
# mask = numpy.array([0, 1, 1, 0, 0], dtype=bool)
# print(arr2[2, mask])


######################修改数组的形态###############

# arr = numpy.arange(12)
# arr1 = arr.reshape(3, 4)
# print(arr1)

# 展平数组 按行展开
# print(arr1.ravel())

# flatten默认按行展开   F按列展开
# print(arr1.flatten())
# print(arr1.flatten('F'))

# 数乘
# arr2 = 3 * arr1
# print(arr2)

# 横向组合
# print(numpy.hstack((arr1, arr2)))
# print(numpy.concatenate((arr1, arr2), axis=1))

# 纵向组合
# print(numpy.vstack((arr1, arr2)))
# print(numpy.concatenate((arr1, arr2), axis=0))

####数组的分割
# arr = numpy.arange(16).reshape(4, 4)

# 横向分割(分成左右)分的个数必须能被列数整除
# print(numpy.hsplit(arr, 2))
# print(numpy.split(arr, 2, axis=1))

# 纵向分割 （分成上下）
# print(numpy.vsplit(arr, 2))


#################################矩阵######################
# 创建矩阵
m1 = numpy.mat('1,1,1;1,2,1;2,1,1')
m = matlib.mat('1,2,3;4,5,6;7,8,9')
# print(m1)
#
m2 = matlib.matrix([[1, 2, 3], [0, 1, 3], [2, 1, 2]])
# print(m2)

arr1 = numpy.eye(3)
# arr2 = 3 * arr1

# 矩阵组合
# m3 = matlib.bmat('arr1 arr2;arr2 arr1')
# print(m3)

# 矩阵相加
# print(m1 + m2)

# 相乘
# print(m1 * m2)

# 矩阵的按位相乘
# print(matlib.multiply(m1, m2))

# 矩阵转置
# print(m1.T)

# 矩阵的逆
# print(m1.I)


#########################数组的运算#############################
# 常见的函数有 四则运算、比较运算、逻辑运算
x1 = numpy.array([1, 2, 3])
x2 = numpy.array([4, 2, 6])

# print(x1 + x2)
# print(x1 - x2)
# print(x1 * x2)
# print(x1 / x2)

# 幂运算
# print(numpy.power(x1, x2))

# 逻辑运算
# all表示and  any表示or
# print(numpy.all(x1 == x2))
# print(numpy.any(x1 == x2))

# 广播机制
a1 = numpy.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
a2 = numpy.array([1, 2, 3])
# print(a1.ndim)
# print(a1 + a2)

######读取文件
# 保存.npy文件
# numpy.save('a1', a1)
##### 保存多个数组
# numpy.savez('a2z', a1, a2)
##### 读取
# print(numpy.load('a1.npy'))

##### 读取多个数组的保存文件
# print(numpy.load('a2z.npz'))
# data = numpy.load('a2z.npz')
# print(data['arr_0'])
# print(data['arr_1'])

# 保存txt文件(默认空格分隔)
# numpy.savetxt('a1.txt', a1, fmt='%d', delimiter=',')
# numpy.savetxt('a1.txt', a1,fmt='%d')

# 读取txt
# print(numpy.loadtxt('a1.txt', delimiter=','))

####################使用函数进行简单的统计分析#################
arr4 = numpy.random.randint(1, 100, size=12)
# print(arr4)
# arr4.shape = 3, 4

# 直接排序
# arr4.sort()
# print(arr4)

# arr4.sort(axis=1)
# print(arr4)
# arr4.sort(axis=0)
# print(arr4)

# 返回重新排序值的下标
# print(arr4.argsort())

###########去重与重复数据#############
# 1数组内数据去重
names = numpy.array(['小明', '小花', '小花', '小明', '小白', '小花', '小白', '小黄', '小黑'])
# print('去重之后的数据', numpy.unique(names))
# print(sorted(set(names)))

# 重复数据(使数组内的数据重复两次)  tile对整个数组进行重复
# print(numpy.tile(names, 2))
# print(arr2)
# 按行重复  repeat对数组元素进行重复
# print(numpy.repeat(arr2, 2, axis=1))

# 按列重复
# print(numpy.repeat(arr2, 2, axis=1))

# print(numpy.tile(arr2, 2))
# print(numpy.repeat(arr2, 2))

#################3###########常用统计函数
####均为聚合计算
arr5 = numpy.arange(16).reshape(2, 8)
# print(arr5)

# 求和
# print(numpy.sum(arr5))

# 纵向求和
# print(numpy.sum(arr5,axis=0))

# h横向求和
# print(numpy.sum(arr5,axis=1))

# 平均值
# print(numpy.mean(arr5))
# print(numpy.mean(arr5, axis=0))
# print(numpy.mean(arr5, axis=1))

# 标准差
# print(numpy.std(arr5))

# 方差
# print(numpy.var(arr5))

# 最小值
# print(numpy.min(arr5))

# print(numpy.min(arr5, axis=1))

####返回最值得索引
# 最小
# print(numpy.argmin(arr5))
# print(numpy.argmin(arr5,axis=0))
# print(numpy.argmin(arr5,axis=1))

# 最大
# print(numpy.argmax(arr5))

########################################
####非聚合计算####
ar1 = numpy.array([4, 2, 5, 6, 3, 8, 9, 6, 3, 5, 4, 2])
print(ar1)
# 累积求和
print(numpy.cumsum(ar1))

# 累积求积
print(numpy.cumprod(ar1))
