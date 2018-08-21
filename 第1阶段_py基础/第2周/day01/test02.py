def add1(a,b):
    c=a*b
    d=a+b
    return c,d
x,y=add1(7,5)
print(x,y)

a=10
def xg(x):
    x=20
xg(a)
print(a)

b=[1,2,3,4,5]
def ax(x):
    x.append(89)
print(b)
ax(b)
print(b)

student = {"001": {"name": "张三", "age": 18, "address": "北京"},
            "002": {"name": "李四", "age": 18, "address": "山东"},
            "003": {"name": "王五", "age": 18, "address": "河北"}}

def zd(zd):
    x={}
    x['name']='小明'
    x['age']=22
    x['address']='上海'
    zd['004']=x
zd(student)
for i,j in student.items():
    print(i,' ',j)

def asf(a,b):
    print('a=',a)
    print('b=',b)
asf(b=123,a=456)

def asd(a,b,c=1111):
    print('a=',a)
    print('b=',b)
    print('c=',c)

def asdf(a,b,**args):
    print('a=',a,end='')
    print('b=',b)
    print('args=',args)
    for i in args.items():
        print(i,' ',j)
asdf(1,2,name='小明',age=4,height=187)

def he(a,b,c):
    sum1=a+b+c
    sum2=a**3+b**3+c**3
    return sum1,sum2

xx,yy=he(1,2,3)
print(xx)
print(yy)