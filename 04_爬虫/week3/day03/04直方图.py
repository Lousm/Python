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

plt.bar(range(3), value[-1, 3:6], width=0.5)
plt.xlabel('产业')
plt.ylabel('产值')
plt.title('2017年第一季度各产业生产总值直方图')
plt.legend(['生产总值'])
plt.xticks(range(3), ['第一产业', '第二产业', '第三产业'])
for x, y in zip(range(3), value[-1, 3:6]):
    plt.text(x, y, y, ha='center',fontsize=12)
plt.show()
