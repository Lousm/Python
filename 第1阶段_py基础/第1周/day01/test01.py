'''
print("你好，python0")
print("你好，python1")
print("你好，python2")
# print("你好，python3")
'''
print("你好，python3.6")


# x=input("请输入一个数:")#input起输入的作用从键盘接受字符
# print("你输入的数字是：",x)

# a=input("请输入你喜欢的水果：")
# print("你喜欢的水果是：",a)
'''
b=1
c=3
d=b/c

print("d=",d)
print(type(d))

e="中公教育"
f=2
# g=f+e
print(type(e))

name="娄世敏"
age=21
height=180
s="我叫{0},今年{4},身高{3},我叫{0}，今年{1}"
print(s.format("小张",30,"小明",160,20))
'''

# print("河南科技学院")
# aa=input("请输入你喜欢的书的名字：")
# print("你喜欢的书是：",aa)


name="张三"
age=21
s="我叫{}，今年{}"
print(s.format(name,age))

s1="我叫{1}，我来自{3}，我今年{2}，我学习{0}"
print(s1.format("python","李四",21,"中国"))

name1="王五"
age1=22
from1="中国"
study1="python"
s2="我叫{name1}，我来自{from1}，我今年{age1}，我学习{study1}"
# s2="我叫{}，我来自{}，我今年{}，我学习{}"
print(s2.format(name1=name1,age1=age1,from1=from1,study1=study1))
'''
x=input("请输入：")
print("输入的类型为：",type(x))
print("已被转换为：",type(float(x)))
'''

a=23
b=3
print("a/b= ",a/b)
print("a//b= ",a//b)
print("a%b= ",a%b)
print("a**b= ",a**b)
'''
x1=input("请输入：")
print("输入的类型为：",type(x1))
print("已被转换为：",type(tuple(x1)))
print(x1)
'''
print("我叫{:*^8},今年{:<8},ppp".format("张三",21))

x=input("请输入：")
print("输入类型为：",type(x))

