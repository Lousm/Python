a1 = ['A', 'B', 'C']
a2 = ['X', 'Y', 'Z']
a3 = []
notarr = ['AX', 'CX', 'CZ']

# BX AZ CY

# 先找出符合题目的所有组合
for i in a1:
    for j in a2:
        if (i + j) not in notarr:
            a3.append(i + j)
print('除不想对战之外的所有组合:')
print(a3)
print()


##########遍历去重（每个字母仅且出现一次）
# 例：组合1 AY 如果A在列表a3中出现了两次，且Y在a3中也出现了两次，则删除组合AY---以此类推
def distinct(arr):
    count1 = 0
    count2 = 0
    sta3 = str(arr)
    for i in arr:
        print('待检测的组合', i)
        for j in sta3:
            if i[:1] == j:
                count1 += 1
            if count1 == 2:
                for k in sta3:
                    if i[1:] == k:
                        count2 += 1
                    if count2 == 2 and count1 == 2:
                        print('删除组合', i)
                        arr.remove(i)
                        count1 = 0
                        count2 = 0
                        print(arr)
                        break
                break
    return arr


asd = len(a3) - len(notarr)


def get_arr(arr):
    if len(arr) == asd:
        return arr
    else:
        return get_arr(distinct(arr))


if __name__ == '__main__':
    print('符合要求的组合：', get_arr(a3))
