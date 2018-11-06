'''
求一个数的阶乘
    递归实现
    非递归实现
'''

def JieC1(n):
    if n==1:
        return 1
    return n*JieC1(n-1)

def JieC2(n):
    a=1
    for i in range(1,n+1):
        a=i*a
    # print("%d的阶乘为%d"%(n,a))
    return a

print(JieC1(20))
print(JieC2(20))