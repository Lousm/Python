a = {"name": '小张', 'age': 21, 'score': 99, 123: "北京"}
print(a['name'])
print(a[123])
print(a.get('name'))

a['name'] = '李四'
a['age'] += 2
a['address'] = '太阳系地球中国'
print(a)

b = dict(name='张三', age=21, tel=110, address='北京')
del b['age']
print(b)

print(a.keys())
print(a.values())

print(a.items())

for i in a.keys():
    print(i)

for i in a.values():
    print(i)

for key, value in a.items():
    print(key, ":", value)


c = {'001': {"name": '小张', 'age': 21, 'score': 99, "address": "北京"},
     '002': {"name": '小明', 'age': 22, 'score': 99, "address": "山东"},
     '003': {"name": '小王', 'age': 23, 'score': 99, "address": "河北"},
     '004': {"name": '小李', 'age': 24, 'score': 99, "address": "北京"}}

for key, value in c.items():
    if value.get('address') == '北京':
        value['house'] = 20
    print(key, ":", value)


d=set((1,2,3,6,5,4,5,6,6,8,9,8))
d1={1,2,3,6,5,4,5,6,6,8,9,8}
print(d)
print(d1)

