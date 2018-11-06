a='this is test text test text test'
b=a.split(' ')
print(b)
cou=0
for i in range(len(b)):
    if b[i]=='test':
        b[i]='new_test'
        print()
        print(b[i])
        cou+=1
    if cou==2:
        break

print(b)