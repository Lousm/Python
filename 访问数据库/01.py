import pymysql

db=pymysql.connect('localhost','root','123456','java1')
cur=db.cursor()
sql='SELECT * FROM node'
try:
    cur.execute(sql)
    res=cur.fetchall()
    for i in res:
        number=i[0]
        xcoord=i[1]
        ycoord=i[2]
        print('number=%d xcoord=%d ycoord=%d'%(number,xcoord,ycoord))
except :
    print('数据错误')

db.close()
