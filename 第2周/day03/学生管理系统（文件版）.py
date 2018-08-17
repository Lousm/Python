class StudentManagement():
    f = open('student.txt', 'a', encoding='utf-8')

    def add(self, num):
        if self.f.readlines().rfind(num) != -1:
            self.num = input("已存在！请输入你要添加的学号：")
        self.name = input("请输入姓名：")
        self.age = input("请输入年龄：")
        self.address = input("请输入地址：")
        self.num = num
        self.st = '\n'+self.num+'   '+self.name+'   '+self.age+'   '+self.address+'\n'
        self.f.write(self.st)
        self.f.close()
 

sm = StudentManagement()
sm.add('004')

a = '001  北京  22  今年'
b = '001'
print(a.rfind(b))
