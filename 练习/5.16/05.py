a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
x = input("请输入第一个数：")
y = input("请输入第二个数：")
x1 = 0
y1 = 0
flag = False
for i in x:
    if i in a:
        flag = True
    else:
        flag = False
        break
for i in y:
    if i in a:
        flag = True
    else:
        flag = False
        break
if flag:
    print(int(x)+int(y))
else:
    print("您输入数据不对")
