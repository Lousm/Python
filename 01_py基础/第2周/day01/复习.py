# 有红、黄、蓝三种颜色的球其中红球3个，黄球3个，绿球6个。先将这12个球混合
#      放在一个盒子中，从中任意摸出8个球，编程计算摸出球的各种颜色搭配
def mq():
    print('%-3s%-3s%-3s'%('红','黄','蓝'))
    for red in range(4):
        for yellow in range(4):
            for blue in range(7):
                if red+yellow+blue==8:
                    print("%-4d%-4d%-4d"%(red,yellow,blue))

mq()

name=['张三']
def asd(n):
    name=n
    print(name)
    def zxc():
        nonlocal name   
        name='李四'
        print(name)
    zxc()
    print(name)

asd('王五')
print(name)

a=[i*10 for i in range(1,13)]
b=[i*3 for i in range(1,13)]
def dfg(a,b):
    c=[]
    for i in range(len(a)):
        c.append(a[i]+b[i])
    return c

print(dfg(a,b))

dic = {'name': '张山', 'age': 23, 'phone': '1383838438', 'address': '北京'}
for i,j in dic.items():
    print(i,j)