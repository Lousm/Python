import pymysql

db=pymysql.connect('localhost','root','123456','java1')
cur=db.cursor()
sql='SELECT * FROM TRUN'
try:
    cur.execute(sql)
    res=cur.fetchall()
    for i in res:
        nid=i[0]
        xcoord=i[1]
        ycoord=i[2]
        buis=i[3]
        tru=i[4]
        energy=i[5]
        state=i[6]
        srand=i[7]
        cid=i[8]
        print('nid=%-3d xcoord=%-3d ycoord=%-3d buis=%-8s tru=%-3d energy=%-3d state=%2s srand=%d cid=%s'%
            (nid,xcoord,ycoord,buis,tru,energy,state,srand,cid))
except :
    print('数据错误')

db.close()