def a(num):
    min=num[0]
    for i in num:
        if i<min:
            min=i
    return(min)

b=[2,6,8,1,63,84]
print(a(b)) 