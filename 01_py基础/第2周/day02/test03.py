class People():
    name = ''
    age = 0
    sex = ''

    def daYin(self):
        print(self.name, self.age, self.sex)


zs = People()
zs.name = '张三'
zs.age = 22
zs.sex = '男'
zs.daYin()

ls = People()
ls.name = '李四'
ls.age = 26
ls.sex = '女'
ls.daYin()


class Student():
    name = ''
    age = 0
    ywScore = 0
    sxScore = 0
    yyScore = 0

    def avg(self):
        return (self.sxScore+self.sxScore+self.yyScore)/3

    def sum(self):
        return self.sxScore+self.sxScore+self.yyScore


stu = Student()
stu.name = '小明'
stu.age = 20
stu.ywScore = 66
stu.sxScore = 77
stu.yyScore = 88
print(stu.avg())
print(stu.sum())

class GirlGriend():
    name=''
    sex='女'
    age=18
    height=165
    weight=100

    # def washTheClothes(self):