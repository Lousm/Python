import pymysql

class Model(object):
    __getduix=None
    def __new__(cls):
        if cls.__getduix==None:
            cls.__getduix=super().__new__(cls)
        return cls.__getduix

    def __init__ (self):
        self.db=pymysql.connect('localhost','root','123456','python0709')
        self.cur=self.db.cursor()

    def getChar(self,a):
        value="`" + a + "`"
        return value

    def getValue(self,a):
        return "'"+ a +"'"

    #添加
    def student1_add(self,*parameter ):
        sql='insert into student1(name,age,sex,tel) values(%s,%s,%s,%s)'
        name=parameter[0]
        age=parameter[1]
        sex=parameter[2]
        tel=parameter[3]
        try:
            self.cur.execute(sql,(name,age,sex,tel))
            self.db.commit()
            print('添加成功')
        except:
            self.db.rollback()
            print("添加失败")

    def student1_del (self,*parameter):
        sql='delete from student1 where {0} = {1}'
        field=self.getChar(parameter[0])
        value=self.getValue(parameter[1])
        print(sql.format(field,value))
        try:
            self.cur.execute(sql.format(field,value))
            self.db.commit()
            print('删除成功')
        except:
            self.db.rollback()
            print("删除失败")

    def student1_upd (self,*parameter):
        sql='update student1 set {0} = {1} where {2} = {3}'
        field1=self.getChar(parameter[0])
        value1=self.getValue(parameter[1])
        field2=self.getChar(parameter[2])
        value2=self.getValue(parameter[3])
        print(sql.format(field1,value1,field2,value2))
        try:
            self.cur.execute(sql.format(field1,value1,field2,value2))
            self.db.commit()
            print('修改成功')
        except:
            self.db.rollback()
            print("修改失败")

model=Model()

# model.student1_add('李雷','2','女','15487659854')
model.student1_del('name','aaa')
# model.student1_upd('name','aaa','name','aaa')