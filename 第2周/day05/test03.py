a = [1, 2, 3]
i = 0
try:
    while i < len(a):
        print(a[i])
        i += 1
    print(5/0)
except:
    print('异常')

raise IndexError('索引异常')