def binarySearch(list, num):
    low = 0  # 要查找的范围
    high = len(list)-1
    while low <= high:  # 只要范围没有缩小到只剩一个函数
        mid = (low+high)//2  # 找到范围中间的数的下标
        a = list[mid]  # 每次猜的数（猜中间值）
        if a == num:  # 找到了元素
            print("找到了，在列表的第%d位" % (mid+1))
            return mid
        elif num < a:  # 猜的数大了（说明要找的数比中间值小，因此将高的范围缩小）
            high = mid-1
        else:
            low = mid+1
    print("不在列表中")
    return None


b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
binarySearch(b, 55)
