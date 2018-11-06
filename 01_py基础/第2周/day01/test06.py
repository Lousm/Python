m=[[1,2,3],[4,5,6],[7,8,9]]
b=[m[i][i] for i in range(len(m))]
print(b)

x=5
def asd():
    x=6
    print(x)
asd()
print(x)

name='张三'
def zxc(name):
    name='lisi'

zxc(name)
print(name)

def qwe(n):
    global name
    name=n
qwe("lisan")
print(name)