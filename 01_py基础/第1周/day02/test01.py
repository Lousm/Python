'''
price=3.5
total=2
money=price*total
name="中公教育"
print("单价：%.2f,%d斤，总额是%.2f，单位%s"%(price,total,money,name))


print("我叫{name},今年{age},来自{from1}".format(name="小明", age=21, from1="中国"))

moeney = 156626
number = 9
everage = moeney//number
yu_e = moeney % number
print("平均每人：%d,剩余：%d" % (everage, yu_e))

print("小明".center(5), "年龄21".ljust(6), "来自中国".rjust(6))

x = "5+4+"
b = "3+2"
print(x)
y = eval("x+b")
print(y)

pi = 3.1415926
a = str(pi)
c = "pi="+a
print(c)

score=float(input("请输入成绩："))
if score>=90:
    print("优秀")
if score>=80:
    print("良好")
elif score>=70:
    print("合格")
elif score>=60:
    print("及格")
else:
    print("不及格")


score=float(input("请输入成绩："))
if score>=90:
    print("优秀")
if 90>score>=80:
    print("良好")
elif 80>score>=70:
    print("合格")
elif 70>score>=60:
    print("及格")
else:
    print("不及格")


weight=float(input("请输入体重："))
if weight>150 :
    print("胖子")
elif weight>130:
    print("还行")
else:
    print("瘦子")


money=float(input("请输入消费金额："))
sex=input("请输入性别：")
if money>10000:
    if sex=="男":
        print("送刮胡刀")
    else:
        print("送化妆品\n小礼物")
else:
    if sex=="男":
        print("送刮胡刀片")
    else:
        print("送化妆品盒")


college = input("请输入大学名称:")
if college == "北京大学":
    LiScore = float(input("请输入理论成绩："))
    JiScore = float(input("请输入技能成绩："))
    AvgScore = (LiScore+JiScore)/2
    if AvgScore > 90:
        print("奖学金：5000")
    elif AvgScore >= 80:
        print("奖学金：3000")
    elif AvgScore >= 60:
        print("奖学金：1000")
elif college == "技能学院":
    EngScore = float(input("请输入英语成绩："))
    if EngScore > 70:
        print("发四级证书")
    CmpScore = float(input("请输入计算机成绩："))
    if CmpScore > 60:
        print("发放计算机国家二级")


money=50
num=1
while money>=10:
    money-=10
    print("吃%d次西瓜,还剩%d"%(num,money))
    num+=1


a=0.09
i=0
while True:
    b=a*2
    a*=2
    i+=1
    if b>=8848:
        break 
print("折了%d,厚度为%.3f"%(i,b))

j = 1
sum = 0
while j <= 10:
    sum += j
    j += 1
print("1-10的和为%d" % sum)


i=30
sum=0
while i<=60:
    sum+=i
    i+=2
print("30-60之间所有的偶数和为%d"%sum)


i=80
sum=0
while i>=65:
    if i%3==0:
        print("%d能被3整除"%i)
        sum+=i
    i-=1
print("能被3整除的和%d"%sum)
'''
print("111111111")
i = 300
sum1 = 0
count = 0
while i <= 500:
    if i % 11 == 0 and i % 17 == 0:
        sum1 += i
        count += 1
    i+=1
print("个数为%d,和为%d" % (count, sum1))


print("222222222")

