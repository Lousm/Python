class Student():
    __slots__ = ['name', 'age', 'weight']  # 来限定class增加的属性

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print('我叫%s，今年%d岁' % (self.name, self.age))


zs = Student('张三', 22)
zs.say()

zs.weight = 120
print(zs.weight)
