import matplotlib.pyplot as plt
import numpy

arr = numpy.load('国民经济核算季度数据.npz')

name = arr['columns']
value = arr['values']

print(value)
# 解决中文不显示
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(10, 10), dpi=80)

# 绘制散点图

# x = value[:, 0]
# y = value[:, 3]
# y2 = value[:, 4]
# y3 = value[:, 5]
#
# plt.scatter(x, y, marker='o', color='r')
# plt.scatter(x, y2, marker='o', color='g')
# plt.scatter(x, y3, marker='o', color='b')
# plt.xlabel('年份')
# plt.ylabel('生产总值（亿元）')
# plt.legend(['第一产业', '第二产业', '第三产业'])
# plt.title('2000-2017年各产业生产总值散点图')
# plt.xticks(value[::4, 0], value[::4, 1], rotation=45)
#
# plt.show()

# # xy刻度
# plt.xticks([-1, 0, 1])
# plt.yticks([-1, 1, 3])

x = value[::4, 0]
y1 = value[::4, 8]
y2 = value[::4, 9]
plt.scatter(x, y1, marker='o', color='g')
plt.scatter(x, y2, marker='o', color='b')
plt.xlabel('年份')
plt.ylabel('生产总值（亿元）')
plt.legend(['建筑行业', '批发零售业'])
plt.title('2000-2017年各产业第一季度生产总值散点图')

# 步长为4
plt.xticks(value[::4, 0], value[::4, 1], rotation=45)

plt.show()
print(x)