count=0
def TowerofHanoi(num, A, B, C):
    if num == 1:
        global count
        count+=1
        print("从 %-2s移动盘子 %-2d号到 %-2s" % (A, num, C))
    else:
        TowerofHanoi(num-1, A, C, B)
        count+=1
        print("从 %-2s移动盘子 %-2d号到 %-2s" % (A, num, C))
        TowerofHanoi(num-1, B, A, C)


num = int(input("请输入层数："))
TowerofHanoi(num, 'A', 'B', 'C')
print('总共交换了 %-2d次'%count)
