arr = []
top = -1

def add():
    global arr
    global top
    data = input("请输入：")
    arr.append(data)
    top += 1
    print(arr)

def jian():
    global top
    global arr
    arr.pop()
    top -= 1
    print(arr)

while True:
    a=input("1,添加  2，弹出")
    if(a=="1"):
        add()
    else:
        jian()