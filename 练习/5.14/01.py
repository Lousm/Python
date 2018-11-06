name='小明'   #用户名称
age=22
email='104043@qq.com'

string1='hello'
string2='word'
print(string1+string2)

numb1=1
numb2=2
print(1+2)

print('Z的ASCII码为：%d'%(ord('Z')))

print('%s'%'admin')

# 8
print('欢迎您：{}您上次登录的时间为{}年{}月{}日'.format('小明',2018,'07',14))

print('欢迎您：{name}您上次登录的时间为{n}年{y}月{r}日'.format(name='小明',n=2018,y='07',r=14))

n=input("姓名：")
a=input("年龄：")
d=input("地址：")
print("我叫%s,我今年%s，我来自%s"%(n,a,d))