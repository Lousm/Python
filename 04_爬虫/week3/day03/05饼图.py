import matplotlib.pyplot as plt
import numpy

arr = numpy.load('国民经济核算季度数据.npz')

name = arr['columns']
value = arr['values']

print(value)
# 解决中文不显示
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(6, 6), dpi=80)

lable = ['第一产业', '第二产业', '第三产业']

explode = [0.01, 0.01, 0.01]  # 饼型之间的距离
plt.pie(value[-1, 3:6], explode=explode, labels=lable, autopct='%1.1f%%')
plt.show()
