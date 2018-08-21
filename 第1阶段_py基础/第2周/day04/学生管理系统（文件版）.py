class StudentManagement():
    def __init__(self, path):
        self.path = path
        with open(self.path, 'r', encoding='utf-8') as fil:
            self.contents = eval(fil.readline())

    def wri(self):
        with open(self.path, 'w', encoding='utf-8') as fil:
            fil.write(str(self.contents))

    def add(self):
        snum = input('请输入你要添加的学号：')
        while True:
            if snum in self.contents:
                snum = input("已存在！请重新输入你要添加的学号：")
            else:
                break
        b = {}
        name = input("请输入姓名：")
        age = input("请输入年龄：")
        address = input("请输入地址：")
        b['name'] = name
        b['age'] = age
        b['address'] = address
        self.contents[snum] = b
        print("添加成功!添加的信息为：%s" % snum, end='')
        print(self.contents.get(snum))

    def change(self):
        snum = input('请输入你要修改的学号：')
        while True:
            if snum not in self.contents:
                snum = input("不存在！请重新输入你要修改的学号：")
            else:
                break
        name = input("请输入要修改的姓名：")
        age = input("请输入要修改的年龄：")
        address = input("请输入要修改的地址：")
        self.contents.get(snum)['name'] = name
        self.contents.get(snum)['age'] = age
        self.contents.get(snum)['address'] = address
        # self.contents[snum] = self.contents.get(snum)
        print("修改成功!修改后的信息为：%s" % snum, end='')
        print(self.contents.get(snum))

    def find(self):
        snum = input("请输入你要查找的学号：")
        while True:
            if snum not in self.contents:
                snum = input("不存在！请重新输入学号：")
            else:
                break
        print("%s的信息为：" % snum, end='')
        print(self.contents.get(snum))

    def delt(self):
        snum = input("请输入你要删除的学号：")
        while True:
            if snum not in self.contents:
                snum = input("不存在！请重新输入你要删除的学号：")
            else:
                break
        del self.contents[snum]
        print("删除成功！", self.contents)


class Start():
    stud = StudentManagement('student.txt')

    def st(self):
        while True:
            oper = input(
                "请输入你要进行的操作：\n\ta.增加学生记录.\n\tb.修改学生记录.\n\tc.删除学生记录.\n\td.查看学生信息.\n\tq.退出学生系统.\n")
            if oper == 'a':
                self.stud.add()
            elif oper == 'b':
                self.stud.change()
            elif oper == 'c':
                self.stud.delt()
            elif oper == 'd':
                self.stud.find()
            else:
                self.stud.wri()
                print('退出系统')
                exit(0)


sta = Start()
sta.st()
