# 左填充和有填充
a = "hello"
print(a.ljust(20, "*"))
print(a.rjust(20, "*"))


def ljust1(st, num, a):
    print(st, end='')
    for i in range(int(num)-len(st)):
        print(a, end='')
    print()


def rjust1(st, num, a):
    for i in range(int(num)-len(st)):
        print(a, end='')
    print(st, end='')
    print()


st = input("请输入字符串：")
num = input("请输入总共长度：")
a = input("请输入补齐的字符：")

ljust1(st, num, a)
rjust1(st, num, a)
