class Animal():
    def jiao(self):
        print('动物会叫')
class Dog(Animal):
    def jiao(self):
        print("汪汪")
class Pig(object):
    def jiao(self):
        print("哼哼")
class Cat(object):
    def jiao(self):
        print("喵喵")

def jiao(a):
    a.jiao()

gou=Dog()
zhu=Pig()
mao=Cat()
jiao(gou)
jiao(zhu)
jiao(mao)