class ren():
    # name=''
    # age=0
    # height=0
    weight = 0

    def say(self):
        print('我叫%s,今年%d,身高%d,私有属性%d' % (self.name, self.age, self.height,self.__qw))

    def __init__(self, name, age, heigth):
        self.name = name
        self.age = age
        self.height = heigth
        ren.weight += 1
        self.__qw=5

    @staticmethod
    def asd():
        print('调用了静态方法')
    
    @classmethod
    def zxc(cls):
        print('调用了类方法')

a = ren('小明', 22, 180)
a.asd()
a.zxc()
a.say()
# print(ren.__qw)

