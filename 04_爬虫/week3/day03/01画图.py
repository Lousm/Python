import matplotlib.pyplot as plt
import numpy

# 1.确定xy的值
x = numpy.linspace(-1, 1, 20)
y = 2 * x + 1
z = x ** 2

# 创建画布
p1 = plt.figure()

# # 画图，传xy
# plt.plot(x, y, 'oy', linewidth=3.0, linestyle='-.', marker='D', markersize=10)
# plt.plot(x, z)
#
# # 解决中文不显示
# plt.rcParams['font.sans-serif'] = 'SimHei'
# plt.rcParams['axes.unicode_minus'] = False
#
# # 添加标题
# plt.title('直线')
# plt.xlabel('x轴')
# plt.ylabel('y轴')
#
# # xy轴的范围
# # plt.xlim((-0.5, 0.5))
# # plt.ylim((0, 2))
#
# # xy刻度
# plt.xticks([-1, 0, 1])
# plt.yticks([-1, 1, 3])
#
# # 图例
# plt.legend(['y=2x+1', 'y=x^2'])
#
# # 边框设置
# xy = plt.gca()  # 获取轴的信息
# xy.spines['right'].set_color('none')
# xy.spines['top'].set_color('none')
#
# # 显示
# plt.show()


####################################
# 两行一列的第一个子图
p1.add_subplot(2, 1, 1)
plt.plot(x, y)
plt.legend(['y=2x+1'])

p1.add_subplot(2, 1, 2)
plt.plot(x, z)
plt.legend(['y=x^2'])

plt.savefig('1_1.jpg')

plt.show()


