st=input("请输入字符：")
'''
for i in st:
    print(i)

i=0
while i<len(st):
    print(st[i])
    i+=1

count=0
for j in st:
    print(j,end=' ')
    count+=1
    if count%3==0:
        print()
'''

k=0
while k<len(st):
    print(st[k],end=' ')
    k+=1
    if k%3==0:
        print()