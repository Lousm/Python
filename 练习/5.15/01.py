print('2的10次方是%d'%(2**10))

yu=101%3

num=int('123')

a=int('0x21',16)
print(a)

# 5
# age=int(input("请输入年龄："))
# sex=input("请输入性别：")
# if age>=18:
#     print('你成年了')
# else:
#     print("未成年")

# if sex=='男':
#     if age>=18:
#         print("可以去玩英雄联盟")
#     else:
#         print("小学生，去玩我的世界")
# else:
#     print("开心消消乐")

i=9
while i>=1:
    j=1
    while j<=i:
        print('%d*%d=%-3d'%(j,i,i*j),end='')
        j+=1
    i-=1
    print()