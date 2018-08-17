a = []

def fullPermutation(a, start, end):
    if start == end:
        for i in a:
            print(i,end='')
        print()
    else:
        for i in range(start, end):
            exchange(a, i, start)
            fullPermutation(a, start+1, end)
            exchange(a, start, i)

def exchange(a, start, end):
    a[start], a[end] = a[end], a[start]

def asd(n):
    start = 0
    end = len(n)
    fullPermutation(n, start, end)

def zxc():
    st = input('请输入一个字符串：')
    for i in st:
        a.append(i)
    asd(a)

zxc()
