import pandas as pd
import numpy

order = pd.read_csv('meal_order_info.csv', sep=',', encoding='gbk')
order['user_time'] = pd.to_datetime(order['use_start_time'])
order['lock_time'] = pd.to_datetime(order['lock_time'])

# 每个客户用餐时间
# 30天内最早的下单时间 和最晚的下单时间 差值
# 每天的平均营业时间

# 1
each_time = order['lock_time'] - order['user_time']
order['time'] = str(order['user_time']).split(' ')[1]
a = []
for i in order['user_time']:
    a.append(str(i).split(' ')[1])
a.sort()
print(a)

# 2
print(order['lock_time'].max() - order['user_time'].min())

# 3
order['lock_time'] = pd.to_datetime(order['lock_time'])
day_1 = [i.day for i in order['use_start_time']]
day_2 = [i.day for i in order['lock_time']]
utime = order['lock_time'].groupby(by=day_2).max() - order['use_start_time'].groupby(by=day_1).min()
print(utime.mean)
