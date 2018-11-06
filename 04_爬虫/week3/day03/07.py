import matplotlib.pyplot as plt
import numpy

p = plt.figure(figsize=(8, 8), dpi=80)

# 解决中文不显示
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

arr = [30, 45, 10, 15]
lable = ['Frogs', 'Logs', 'Dogs', 'Hogs']
explode = [0.06, 0, 0, 0]
plt.pie(arr, explode=explode, labels=lable, autopct='%1.1f%%',shadow=True,startangle=135)
plt.show()
