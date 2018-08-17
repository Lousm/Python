# 水仙花数
def isShuiXianHua(i):
    a = i//100
    b = i//10 % 10
    c = i % 10
    if a**3+b**3+c**3 == i:
        print("%d是水仙花数" % i)


def isShuiXianHua2(i):
    sum1 = 0
    temp = i
    while temp > 0:
        sum1 += (temp % 10)**3
        temp //= 10
    if sum1 == i:
        print("%d是水仙花数" % i)


for i in range(100, 1000):
    isShuiXianHua(i)
    isShuiXianHua2(i)

# 写一个函数，识别是否字符串符合python语法的变量名


def isLegal(st):
    i = ord(st[0])
    if 65 <= i <= 90 or i == 95 or 97 <= i <= 122:  # 首先判断第一位是否是字母或下划线
        for j in st:  # 再依此判断每一位
            a = ord(j)
            if not (65 <= a <= 90 and a == 95 and 97 <= a <= 122 and 48 <= a <= 57):
                print("输入的字符为%s,含非法字符不符合变量名命名要求！！" % st)
        print("字符串符合变量名命名规则")
    else:
        print("输入的字符为%s,含非法字符不符合变量名命名要求！！" % st)


# isLegal(input("请输入一个字符串："))

# 对100以内的两位数，请使用一个两重循环打印出所有十位数数字比个位数数字小的数，例如，23（2 < 3）。


def isGreaterThan():
    for i in range(10):
        for j in range(10):
            if i > j:
                print(str(i)+str(j))


isGreaterThan()


sets = {1, 2, 3, 4, 5}
sets2 = {4, 5, 6, 7}
sets3={11,12,13}
print(sets.union(sets2))  # 返回sets和sets2的合集
print(sets.intersection(sets2))  # 返回sets和sets2的交集
print(sets.difference(sets2))  # 返回在sets中，而不在sets2中的集合
print(sets.symmetric_difference(sets2))  # 返回在sets和sets2中没有同时存在的值

a=[[1,2,3],[4,5,6],[7,8,9]]
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        print(a[i][j],end=(" "))
        j+=1
    i+=1
    print()

for i in a:
    for j in i:
        print(j, end=' ')
    print()

print(sets.issuperset(sets2))
print(sets2.issubset(sets))
print(sets3.isdisjoint(sets))
