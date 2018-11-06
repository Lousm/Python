a = [1, 2, 3, 4, 5, 6, 7, 12, 58, 16, 85, 32]


def jishu(a):
    for i in range(len(a)):
        if a[i] % 2 == 1:
            a[i] *= 2


def gewei(a):
    for i in range(len(a)):
        if a[i] > 10:
            a[i] %= 10


jishu(a)
gewei(a)
print(a)
