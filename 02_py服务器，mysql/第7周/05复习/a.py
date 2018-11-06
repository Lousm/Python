
a=['飞机','火车','高铁','自行车','牙膏','牙刷','毛巾',1.12,1.5,4,6]
b=['飞机','火车','高铁','自行车']
c=['牙膏','牙刷','毛巾']
s=len(a)-1
for i in range(s) :
    print(type(a[i]))
    if a[i] in b :
            print(a[i]+'是交通工具')
    elif a[i] in c :
            print(a[i]+'是生活用品')
    elif type(a[i]) == float :
            print(a[i]+'是小数')
    elif type(a[i]) == int :
            print(a[i]+'是整数')
    # elif type(a)== list:
    #     print('a是列表')


