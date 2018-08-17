i=1
while i<=10:
    score=int(input("请输入第%d个学生的成绩："%(i)))
    if not(60<score<100):
        continue
    i+=1

