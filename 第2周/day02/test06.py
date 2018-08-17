def asd(n):
    f=open(n,'a',encoding='utf-8')
    while True:
        b=input("请输入姓名：")
        if b=='0':
            f.close()
            exit(0)
        f.write(b)
        f.write('\n')
asd('data.txt')