a=[x for x in range(101)]
count=0
def coun(a):
    if len(a)==0:
        return 0
    else:
        global count
        count+=1
        coun(a[:-1])
        return count
print(coun(a))