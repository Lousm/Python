from math import *
a=input("请输入一个数：")
'''
b=int(a)
count=0
for i in a:
    count+=1
print("整数长度为：%d"%count)

# print(len(a))
# print(b)
count1=0
while True:
    b=b//10
    count1+=1
    if b==0:
        break
print("整数长度为：%d"%count1)

# 整除10，再对10取余得到的是10位
c=int(a)//10%10
print(c)

if len(a)>=2:
    if c%2==0:
        print("输入的数是%d，十位数是偶数"%int(a))
    else:
        print("输入的数是%d，十位数是奇数"%int(a))
else:
    print("请输入两位或两位以上的数")

if c%2==0:
    print("输入的数是%d，十位数是偶数"%int(a))
else:
    print("输入的数是%d，十位数是奇数"%int(a))
'''

# 抹零
# j=1
# for i in len(a)-1:
#     j*=10
d=float(a)//10*10
# d=math.floor(float(a))
print(float(a))
print("应付%f,实付%d"%(float(a),d))

