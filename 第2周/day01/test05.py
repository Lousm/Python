a = [i*10 for i in range(1, 13)]
b = [i*2 for i in range(1, 13)]


def sy(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i]+b[i])
    return c


c = sy(a, b)
print(c)
