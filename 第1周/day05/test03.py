# 直角三角形
def zj(n):
    for i in range(n):
        for j in range(n-i):
            print(end=' ')
        for j in range(i+1):
            print("*", end='')
        print()


zj(7)  # 行数

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

# n = int(input('输入层数'))
n = 6
width = 2 * n - 1
for i in range(1, n):
    num = 2*i - 1
    str_l = '*' * num
    print(str_l.center(width, ' '))


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
'''
# 每次递进去输出，每次回溯输出
def sx(n):
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
    sx(n-1)
    if n==0:
        return n

sx(7)
'''