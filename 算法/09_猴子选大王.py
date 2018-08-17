def monkey():
    a = []
    monkey_num = int(input('请输入猴子数量：'))
    num = int(input('请输入数到第几个踢猴子：'))
    for i in range(monkey_num):
        a.append(1)  # 猴子初始值为1
    leftnum = monkey_num  # 剩余猴子总数
    count = 0
    index = 0
    while leftnum != 1:
        if a[index] == 1:
            count += 1
            if count == num:
                a[index] = 0  # 踢出去的设置该值为0
                count = 0
                leftnum -= 1
        index += 1
        if index == len(a):
            index = 0
    for i in range(len(a)):
        if a[i] == 1:
            print('第%d只猴子被选为大王' % (i+1))
monkey()
