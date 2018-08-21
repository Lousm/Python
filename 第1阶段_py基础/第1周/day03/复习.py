#求字符串长度
# sLen=input("请输入一个字符串：")
sLen="北京欢迎你"
count1=0
for i in sLen:
    count1+=1
print("字符串长度为：%d"%count1)

a=0
count2=0
while a<len(sLen):
    count2+=1
    a+=1
print("字符串长度为：%d"%count2)

#判断十位的奇偶
sub=4567
sw=sub//10%10
if sw%2==0:
    print("%d的十位数是偶数")
else:
    print("%d的十位数是奇数")

# 抹零
money=166.542
mon=money//10*10
print(mon)
print("应付%f,实付%d"%(money,mon))

# 99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%-3d"%(i,j,i*j),end='')
    print()

i1=1
while i1<10:
    j1=1
    while j1<=i1:
        print("%d*%d=%-3d"%(i1,j1,i1*j1),end='')
        j1+=1
    i1+=1
    print()

# while由用户控制结束
while True:
    # a=input("请输入密码：")
    a=123456
    if int(a)==123456:
        print("密码正确")
        break
    print("密码错误请重新输入！")

# 字符串操作
st="新时代中国特色社会主义"
    # 字符串长度
count3=0
for i in st:
    count3+=1
print("字符串长度为：%d"%count3)
    # 逐个打印字符
for i in st:
    print(i)