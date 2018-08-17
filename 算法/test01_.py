a=[5,6,2,8,8,85,6612,85,24]
m=0
def max(a):
    global m
    if len(a)==0:
        return 0
    else:
        if a[0]>m:
            m=a[0]
        max(a[1:len(a)])
        return m
print(max(a))
