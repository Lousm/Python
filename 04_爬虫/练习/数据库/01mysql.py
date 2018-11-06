import pymysql

data = {
    'id': '20151515143',
    'name': '小明',
    'age': 22
}
table = 'student'
keys = ','.join(data.keys())
values = ','.join(['%s'] * len(data))

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='images360')
cursor = db.cursor()
sql = "insert into {table} ({keys}) values ({values})".format(table=table, keys=keys, values=values)

# try:
#     if cursor.execute(sql, tuple(data.values())):
#         print('插入成功')
#         db.commit()
# except:
#     print('插入失败')
#     db.rollback()
# db.close()

sql1 = 'select * from student where age>=20'

try:
    cursor.execute(sql1)
    print(cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print(row)
        row = cursor.fetchone()
except:
    print('Error')
