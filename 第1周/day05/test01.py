a = 'abcdefg'
for x in a:
    print(x, end='|')
print()
i = 0
while i < len(a):
    print(a[i], end='|')
    i += 1
print()

a1 = ['张三', '李四', '北京', '天津', '上海']
for x in a1:
    print(x, end='|')
print()
i1=0
while i1<len(a1):
    print(a1[i1])
    i1+=1

for x,y in enumerate(a):
    print(x,':',y)