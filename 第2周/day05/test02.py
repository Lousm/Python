class Student():
    def __init__ (self):
        self.__name=''
        self.__age=0
    def setname (self,name):
        self.__name=name
    def getname (self):
        return self.__name
    
    def setage (self,age):
        if not isinstance(age,int):
            print('错误')
            age=0
        self.__age=age
    def getage (self):
        return self.__age
    
    name=property(getname,setname)
    age=property(getage,setage)

stu=Student()
stu.age=22
stu.name='李四'
print(stu.age)
print(stu.name)