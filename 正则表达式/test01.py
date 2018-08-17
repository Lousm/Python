f=open("01.txt",'r',encoding='utf-8')
for i in f:
    if not i.startswith("www"):
        print(i)