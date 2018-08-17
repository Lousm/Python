# 穿插字符串
def zifu():
    a = [1, 2, 3, 4, 5, 6, 7]
    b = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100, 110, 120, 130, 140]
    d = []
    i = 0
    maxlen = 0
    minlen = 0
    if len(a) < len(b):
        maxlen = len(b)
        minlen = len(a)
    else:
        maxlen = len(a)
        minlen = len(b)
        b,a=a,b
    while i < maxlen:
        if i < minlen:
            d.append(a[i])
        d.append(b[i])
        i += 1
    print(d)


zifu()
# 学生管理
a = {'001': {"name": '小张', 'age': 21,  "address": "北京"},
     '002': {"name": '小明', 'age': 22,  "address": "山东"},
     '003': {"name": '小王', 'age': 23,  "address": "河北"},
     '004': {"name": '小李', 'age': 24,  "address": "北京"}}


def add():
    snum = input("请输入你要添加的学号：")
    while True:
        if snum in a:
            snum = input("已存在！请输入你要添加的学号：")
        else:
            break
    b = {}
    name = input("请输入姓名：")
    age = input("请输入年龄：")
    address = input("请输入地址：")
    b['name'] = name
    b['age'] = age
    b['address'] = address
    a[snum] = b
    print("添加成功!添加的信息为：%s" % snum, end='')
    print(a.get(snum))


def change():
    b = {}
    snum = input("请输入你要修改的学号：")
    while True:
        if snum not in a:
            snum = input("不存在！请输入你要修改的学号：")
        else:
            break
    name = input("请输入要修改的姓名：")
    age = input("请输入要修改的年龄：")
    address = input("请输入要修改的地址：")
    a.get(snum)['name'] = name
    a.get(snum)['age'] = age
    a.get(snum)['address'] = address
    a[snum] = a.get(snum)
    print("修改成功!修改后的信息为：%s" % snum, end='')
    print(a.get(snum))


def find():
    snum = input("请输入你要查找的学号：")
    while True:
        if snum not in a:
            snum = input("不存在！请重新输入学号：")
        else:
            break
    print("%s的信息为：" % snum, end='')
    print(a.get(snum))


def delt():
    snum = input("请输入你要删除的学号：")
    while True:
        if snum not in a:
            snum = input("不存在！请重新输入你要删除的学号：")
        else:
            break
    del a[snum]
    print("删除成功！", a)


def start():
    while True:
        oper = input(
            "请输入你要进行的操作：\n\ta.增加学生记录.\n\tb.修改学生记录.\n\tc.删除学生记录.\n\td.查看学生信息.\n\tq.退出学生系统.\n")
        if oper == 'a':
            add()
        elif oper == 'b':
            change()
        elif oper == 'c':
            delt()
        elif oper == 'd':
            find()
        else:
            exit(0)


start()

# 空心三角


def kx(n):
    x = (n+1)*2  # 总位数
    l = x//2  # 左空格
    num = 1  # *的个数
    for i in range(n):
        for j in range(l):
            print(end=' ')
        l -= 1
        if num == 1:  # 第一行
            print("*", end='')
            num += 2
        elif i == n-1:  # 最后一行
            for j in range(num):
                print("*", end='')
            num += 2
        else:  # 中间空格数
            print("*", end='')
            for j in range(num-2):
                print(end=' ')
            print("*", end='')
            num += 2
        print()


kx(15)

# 等腰三角形


def dy(n):
    x = (n+1)*2  # 总位数
    l = x//2  # 左空格
    num = 1  # *的个数
    for i in range(n):
        for j in range(l):
            print(end=' ')
        l -= 1
        for j in range(num):
            print("*", end='')
        num += 2
        print()


dy(6)

# 直角三角形


def zj(n):
    for i in range(n):
        for j in range(n-i):
            print(end=' ')
        for j in range(i+1):
            print("*", end='')
        print()


zj(7)  # 行数

