# f=open('01.txt','w')
# f.write('12345')
# print(f.tell())
# f.write('asdf')
# print(f.tell())
# f.close()

f1=open('01.txt','r')
print(f1.readline())
f1.seek(0,0)
print(f1.readline())
f1.close()

with open('01.txt') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())
