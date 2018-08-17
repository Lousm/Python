def fbnq(max):
    n,a,b=0,0,1
    while n<max:
        a,b=b,a+b
        yield a   #返回a后，函数挂起，下次调用从此处继续执行(还在循环里)
        n+=1

x=fbnq(8)

for i in x:
    print(i)