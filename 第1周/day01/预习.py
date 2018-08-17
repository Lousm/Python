'''
x=int(input("请输入一个大于10并且小于50的数字："))
control=True
while control:
    if x>10 and x<50:
        print("输入正确，您输入的数字是：",x)
        control=False
    else:
        x=int(input("输入错误，请重新输入："))    


x=input("请输入一个字符：")
control=True
while control:
    print("输入字符的ascii码是：",ord(x))
    # control=False
    x=input("再输入一个：")
'''

i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d*%d=%-3d" % (j, i, i*j), end='')
        j += 1
    print('\n')
    i += 1



for a in range(1,10):
    b = 1
    for b in range(1,a+1):
        print("%d*%d=%-3d" % (b, a, a*b), end='')
        b += 1
    print('\n')
    a += 1



cars=["bmw","byd","qq"]
car=input("请输入一个汽车品牌：")
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

