# 穿插字符串
a=[1,3,5,7,9]
b=[2,4,6,8,10]
d=[]
j=0
for i in a:
    d.append(i)
    for j in range(len(b)):
        d.append(b[j])
        break
    j+=1
    print(j)
print(d)

# 列表一样长
# x=0
# while x<len(a):
#     d.append(a[x])
#     d.append(a[x])
# print(d)
e=[]
i1=len(a)-1
j1=0
while i1>=0:
    e.append(a[j1])
    e.append(b[i1])
    j1+=1
    i1-=1
print(e)