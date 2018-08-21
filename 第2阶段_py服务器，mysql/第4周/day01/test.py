def a():
    n=1
    print(111)
    yield n
    
    n+=1
    print(222)
    yield n

    n+=1
    print(333)
    yield n

b=a()
print(next(b))
print(next(b))
print(next(b))

c=a()
for i in c:
    print(i)