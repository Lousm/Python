a = [i for i in range(5)]
print(a)

a1 = [i for i in range(100, 221) if i % 2 == 1]
print(a1)

a2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in a2:
    for j in i:
        print(j, end=' ')
    print()

# 排序，倒叙：冒泡


def theMpSort():
    a3 = [1, 2, 3, 4, 50, 6, 7, 8, 9]
    for i in range(len(a3)):
        for j in range(i, len(a3)):
            if a3[i] < a3[j]:
                a3[i], a3[j] = a3[j], a3[i]
    print(a3)


theMpSort()


def theXzSort():
    a3 = [1, 2, 3, 4, 50, 6, 7, 8, 9]
    for i in range(len(a3)):
        max = i
        for j in range(i, len(a3)):
            if a3[j] > a3[max]:
                max=j
            a3[i],a3[max]=a3[max],a3[i]
    print(a3)


theXzSort()
