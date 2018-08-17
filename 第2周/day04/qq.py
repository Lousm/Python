class Oper():
    def __init__(self,path):
        self.path=path
        self.contents=self.readfile()
    def readfile(self):
        with open(self.path,"r",encoding='utf-8') as file:
            c=file.readline()
            print(c)
            return eval(c)
    def writefile(self):
        with open(self.path,"w",encoding='utf-8') as file:
            file.write(str(self.contents))
    def addStudent(self):
        num=input("输入学号:")
        if num in self.contents:
            print("学号已存在")
        else:
            zd={}
            zd["name"]=input("输入姓名:")
            zd["age"]=input("输入年龄:")
            zd["address"]=input("输入住址")
            self.contents[num]=zd
        print(self.contents)
    def updateStudent(self):
        num=input("输入学号:")
        if num in self.contents:
           self.contents[num]["name"]=input("输入新姓名")
           self.contents[num]["age"]=input("输入新年龄")
           self.contents[num]["address"]=input("输入新住址")
           print(self.contents)
        else:
            print("编号不存在")
    def deleteStudent(self):
        num=input("输入学号:")
        if num not in self.contents:
            print("编号不存在")
        else:
            del self.contents[num]
        print(self.contents)
    def searchStudent(self):
        num=input("输入学号:")
        if num not in self.contents:
            print("编号不存在")
        else:
            for key,value in self.contents[num].items():
                print(key,":",value)
        print(self.contents)
one=Oper("student.txt")

while True:
    num2=int(input("输入操作编号:"))
    if num2==1:
        one.addStudent()
    elif num2==2:
        one.updateStudent()
    elif num2==3:
        one.deleteStudent()
    elif num2==4:
        one.searchStudent()
    elif num2==0:
        one.writefile()
        exit(0)
isinstance
