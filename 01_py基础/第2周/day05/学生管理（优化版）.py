class Student():
    def __init__(self, path):
        self.path = path
        self.b = []
        with open(self.path, 'r', encoding='utf-8') as file:
            self.a = eval(file.readline())
        for i in range(len(self.a)):
            self.b = self.a[i]['num']

    def wri(self):
        with open(self.path, 'w', encoding='utf-8') as file:
            file.write(str(self.a))

    def isExist(self, i):
        self.sid = input('请输入学号：')
        while True:
            if i == 'add':
                if self.sid in self.b:
                    self.sid = input('已存在！请重新输入：')
                else:
                    break
            else:
                if self.sid not in self.b:
                    self.sid = input('不存在！请重新输入：')
                else:
                    break

    def gain(self):
        self.name = input("请输入姓名：")
        self.age = input("请输入年龄：")
        self.address = input("请输入住址：")

    def add(self):
        self.isExist('add')
        self.gain()
        c = {}
        c['num'] = self.sid
        c['name'] = self.name
        c['age'] = self.age
        c['address'] = self.address
        self.a.append(c)
        self.b.append(self.sid)
        print("添加成功!添加的信息为：%s" % self.a[len(self.a)-1])

    def change(self):
        self.isExist('change')
        self.gain()
        index = self.b.index(self.sid)
        self.a[index]['name'] = self.name
        self.a[index]['age'] = self.age
        self.a[index]['address'] = self.address
        print("修改成功!修改后的信息为：%s" % self.a[index])

    def find(self):
        self.isExist('find')
        index = self.b.index[self.sid]
        self.a[index]
        print("查找成功!查找到的信息为：%s" % self.a[index])

    def delt(self):
        self.isExist('delt')
        index = self.b.index[self.sid]
        self.a.pop(index)
        self.b.remove(self.sid)
        print("删除成功！", self.a)


class Main(object):
    stud = Student('student2.5.txt')

    def start(self):
        while True:
            print('==============================学生管理系统==============================')
            oper = input(
                "请输入你要进行的操作：\n\t1.增加学生记录.\n\t2.修改学生记录.\n\t3.删除学生记录.\n\t4.查看学生信息.\n\t0.退出学生系统.\n")
            print(
                '=======================================================================')
            if oper == '1':
                self.stud.add()
            elif oper == '2':
                self.stud.change()
            elif oper == '3':
                self.stud.delt()
            elif oper == '4':
                self.stud.find()
            else:
                print('程序退出')
                self.stud.wri()
                exit(0)


main = Main()
main.start()
