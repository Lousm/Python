'''
for i in range(1, 9):
    print(i, end='')
'''

for i in range(18, 26):
    if i % 2 != 0:
        print(i, end=' ')
print()          
for i in range(18, 26,2):
    print(i+1, end=' ')

for a in range(1,10):
    b = 1
    for b in range(1,a+1):
        print("%d*%d=%-3d" % (b, a, a*b), end='')
        b += 1
    print('\n')
    a += 1

k=1
while k<4:
    j=1
    while j<=4-k:
        print("*",end='')
        j+=1
    print()
    k+=1

for i in range(1,4):
    for j in range(4-i):
        print("*",end='')
    print()

while True:
    x=input("请输入成绩：")
    if int(x)==0:
        print("结束输入")
        break
    print("输入的成绩是：",x)