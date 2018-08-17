import random
a=[]
for i in range(100):
    a.append(random.randint(1,500))
print(a)

def kuaisu(a):
    if len(a)<2:
        return a
    else:
        zhongjian=a[0]
        left=[i for i in a[1:] if i<=zhongjian]
        right=[i for i in a[1:] if i>zhongjian]
        return kuaisu(left)+[zhongjian]+kuaisu(right)

print(kuaisu(a))