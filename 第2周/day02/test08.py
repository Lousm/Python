set1={''}
def count1(n):
    max1=0
    for i in range(len(n)):
        count2=0
        for j in n:
            if n[i]==j:#先将第一个依此跟余下的每个进行比较看是否相同
                count2+=1
                if i==0:#并且先将第1个字符出现的次数给最大的
                    max1+=1
        if max1<=count2:#如果max小于等于下一个字符出现的次数，交换，并将count2重置为0
            max1,count2=count2,max1
            if max1==count2:#将出先次数相同的字符存到集合
               set1.add(n[i])
    return max1
n=input('请输入一个字符串：')
x=count1(n)
print('以下字符出现次数最多，出现次数为%d'%x)
set1.remove('')
for i in set1:
    print(i)
            