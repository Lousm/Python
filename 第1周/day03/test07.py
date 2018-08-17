a="abcdefgh"
print(a[len(a)-1])#字符串最后一位
print(a[-1])

print(a[0:3])
print(a[2:4])
print(a[:-1])

print(a[2:-1:4])

b='123456789'
x=b.find('123',2,8)
print(x)

c='我叫小明，我来自东北，我21'
print(c)
d=c.replace("小明","老王")
e=c.replace("我","ni",3)
print(d)
print(e)

f="bei jing huan ying ni"
g=f.split(' ')
print(g)

h="2018-07-11"
j=h.split("-")
print(j)

f1=f.capitalize()
print(f1)

f2=f.title()
print(f2)

f3=f.startswith("bei")
print(f3)

a1=[1,2,3,4,5,6,7,8]
print(a1[2])

# sum1=0
# for i in a1:
#     print(i)
#       sum1+=int(i)
# print(sum1)

a2=[10,20,22,"beijing",True,[1,2,3,4]]
for i in a2:
    print(i)

a2.append(444)
print(a2)

a2.insert(3,444)
print(a2)

