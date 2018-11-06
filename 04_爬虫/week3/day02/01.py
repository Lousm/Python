import numpy

arr = numpy.loadtxt('len.csv')

# 求和
print('求和')
print(numpy.sum(arr))
print()

# 累计求和
print('累积求和')
print(numpy.cumsum(arr))
print()

# 均值
print('均值')
print(numpy.mean(arr))
print()

# 方差
print('方差')
print(numpy.var(arr))
print()

# 标准差
print('标准差')
print(numpy.std(arr))
print()

#最大值
print('最大值')
print(numpy.max(arr))
print()

#最小值
print('最小值')
print(numpy.min(arr))
print()

#最大值索引
print('最大值索引')
print(numpy.argmax(arr))
print()

#最小值索引
print('最小值索引')
print(numpy.argmin(arr))
print()

# 排序
print('排序')
# arr.sort()
print(arr)
print()

# 去重
print('去重')
print(numpy.unique(arr))
print()