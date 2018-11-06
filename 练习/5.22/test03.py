def a():
    f=open('5.22.03.txt','w',encoding='utf-8')
    for i in range(1,100):
        if i%2==1:
            f.write(str(i)+' ')
    f.close()
a()