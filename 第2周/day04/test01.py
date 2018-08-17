a=[1,2,3,4,5]
b=iter(a)

try:
    print(next(b))

except :
    print('出错')
    exit(0)