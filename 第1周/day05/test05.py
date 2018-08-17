# 找素数
def isSuShu(x,y):
    for i in range(x,y+1):
        yu=0
        for j in range(2,i+1//2):
            if i%j==0:
                yu=1
                break
        if yu==0:
            print("%d是素数"%i)
a,b=input("请输入范围(初值大于2)：").split(' ')
a1=int(a)
b1=int(b)
isSuShu(a1,b1)
