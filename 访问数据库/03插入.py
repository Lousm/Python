import pymysql

db=pymysql.connect('localhost','root','123456','python0709')
cur=db.cursor()

while True:
    name,age,sex,tel=input('请输入要插入的姓名，年龄，性别，用空格分开：').split()
    sql='insert into student1(name,age,sex,tel) values(%s,%s,%s,%s)'
    try:
        cur.execute(sql,(name,age,sex,tel))
        db.commit()
    except:
        db.rollback()
        print('错误')
db.close()
