# 水仙花数
def isShuiXianHua(x):
    bai = x//100
    shi = x % 100//10
    # shi = x //10%10
    ge = x % 10
    if bai**3+shi**3+ge**3 == x:
        print("%d是水仙花" % x)


def isShuiXianHua2(x):
    sum = 0
    temp = x
    while temp:
        sum += (temp % 10)**3  
        temp //= 10     # 注意这里要使用地板除
    if sum == x:
        print("%d是水仙花" % x)


# a=input("请输入一个")
for i in range(100, 1000):
    isShuiXianHua(i)
    isShuiXianHua2(i)
