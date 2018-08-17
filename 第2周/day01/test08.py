def jc(n):
    if n == 1:
        return 1
    else:
        return n*jc(n-1)


print(jc(5))


def fbnq(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fbnq(n-1)+fbnq(n-2)


print(fbnq(5))


def asd(n):
    for i in range(1, n+1):
        print(fbnq(i))


asd(12)
