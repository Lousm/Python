a=['a','b','c',['d','e','f',['g','h','i',['j','k','l',['m','n','o',['p','q','r',['s','t','u',['v','w','x',['y','z']]]]]]]]]
b=[]
def funcname(a):
    for i in a:
        if type(i)!=list:
            print(i,end=' ')
            global b
            b.append(i)
        else:
            return funcname(a[len(a)-1])
    if type(a[len(a)-1])!=list :
        return 
        
funcname(a)
print(b)
