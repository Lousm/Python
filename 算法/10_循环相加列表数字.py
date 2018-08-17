a=[x for x in range(101)]
def sum(a):
    if len(a)==0:
        return 0
    else:
        return a[0]+sum(a[1:len(a)])

print(sum(a))
