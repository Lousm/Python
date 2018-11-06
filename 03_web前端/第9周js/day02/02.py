import random
import time
import threading
arr=[]
sum=int(input("请指定随机数个数："))
def shuzu(arr):
    arr.clear()
    start=time.time()
    for i in range(sum):
        arr.append(random.randint(1,30000000))
    end=time.time()
    print("生成随机数用时：%f"%(end-start))

#冒泡排序
def maopao(arr):
    for i in range(len(arr)):
        for j in range(i):
            if arr[i]<arr[j]:
                arr[i],arr[j]=arr[j],arr[i]

#快速排序
def kuaisu(arr):
    if len(arr)<2:
        return arr
    else:
        center=arr[0]
        left=[i for i in arr[1:] if i<=center]
        right=[i for i in arr[1:] if i>center]
        return kuaisu(left)+[center]+kuaisu(right)
        
def kuai():
    shuzu(arr)
    start1=time.time()
    arr1=kuaisu(arr)
    end1=time.time()
    print("%d个随机数，快速排序用时%f"%(sum,end1-start1))

def mao():
    shuzu(arr)
    start2=time.time()
    maopao(arr)
    end2=time.time()
    print("%d个随机数，冒泡排序用时%f"%(sum,end2-start2))

# with open("./2.txt","w") as f:
#     f.write(str(arr1))

def main():
    t1=threading.Thread(target=kuai())
    t2=threading.Thread(target=mao())
    t1.start()
    t2.start()

if __name__ == '__main__':
    main()