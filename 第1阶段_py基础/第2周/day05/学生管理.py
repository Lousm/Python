class Student():
    def __init__(self, path):
        self.path = path
        self.b = []
        with open(self.path, 'r', encoding='utf-8') as fil:
            self.a = eval(fil.readline())
            print(self.a)
            print(type(self.a))
        for i in range(len(self.a)):
            self.b.append(self.a[i]['num'])

    def wri(self):
        with open(self.path, 'w', encoding='utf-8') as fil:
            fil.write(str(self.a))

    def isExist(self, i):  # 根据操作判断id存在还是不存在
        self.sid = input('请输入学号：')
        while True:
            if i == 'add':
                if self.sid in self.b:
                    self.sid = input('已存在！请重新输入学号：')
                else:
                    break
            else:
                if self.sid not in self.b:
                    self.sid = input('不存在！请重新输入学号：')
                else:
                    break

    def gain(self):
        self.name = input('请输入姓名：')
        self.age = input('请输入年龄：')
        self.address = input('请输入地址：')

    def add(self):
        self.isExist('add')
        self.gain()
        d = {}
        d['num'] = self.sid
        d['name'] = self.name
        d['age'] = self.age
        d['address'] = self.address
        self.a.append(d)
        self.b.append(self.sid)
        print("添加成功!添加的信息为：%s" % self.a[len(self.a)-1])

    def change(self):
        self.isExist('change')
        self.gain()
        x = self.b.index(self.sid)
        self.a[x]['name'] = self.name
        self.a[x]['age'] = self.age
        self.a[x]['address'] = self.address
        self.a[x]['num'] = self.sid
        print("修改成功!修改后的信息为：%s" % self.a[x])
        # self.print1('change')

    def find(self):
        self.isExist('find')
        x = self.b.index(self.sid)
        print("查找成功!查找到的信息为：%s" % self.a[x])

    def delt(self):
        self.isExist('delt')
        x = self.b.index(self.sid)
        self.a.pop(x)
        self.b.remove(self.sid)
        print("删除成功！", self.a)


class Start():
    stud = Student('student2.5.txt')

    def st(self):
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
                self.stud.wri()
                print('退出系统')
                exit(0)


sta = Start()
sta.st()
