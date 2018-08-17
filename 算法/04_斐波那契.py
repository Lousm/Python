def Fibonacci(n):
    if n==1 or n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

def a(n):
    for i in range(1,n+1):
        print('%3d'%i,end='  ')
        print('%-3d'%(Fibonacci(i)))

a(12)