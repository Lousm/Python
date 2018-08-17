def isDaXiao(arr):  # 找最小值
    min = arr[0]
    min_index = 0
    for i in range(1, len(arr)):
        if a[i] < min:
            min = a[i]
            min_index = i
    return min_index  # 返回最小值的下标


def sort1(arr):
    b = []
    for i in range(len(arr)):
        min = isDaXiao(arr)
        b.append(arr.pop(min))
    return b


a = [66, 84, 51, 39, 23, 551, 4561, 6513, 1213, 1165, 54, 33, 484, 6651, 222]
print(sort1(a))
