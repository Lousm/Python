def a(f):
    count=0
    fil=open(f,'r',encoding='utf-8')
    for i in fil:
        count+=1
    return count

print(a('5.22.07.txt'))