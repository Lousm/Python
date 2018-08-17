class Dog():
    def jiao(self):
        print('这是一只%s,%s血统，颜色是%s' % (self.pz, self.__xt, self.color))

    def __init__(self, color, pz, __xt):
        self.color = color
        self.pz = pz
        self.__xt = __xt


dog = Dog('黑白', '哈士奇', '皇家血统')

dog.jiao()


class Hsq(Dog):
    def __init__(self, weight, color, pz, __xt):
        self.weight = weight

        Dog.__init__(self, color, pz, __xt)

    def say(self):
        # Dog.jiao(self)
        print('这只狗的体重是%d' % self.weight)


hsq = Hsq(120, '黑白', '哈士奇', '皇家血统')
hsq.say()

print(isinstance(hsq,Hsq))
print(isinstance(hsq,Dog))
print(isinstance(dog,Dog))
print(isinstance(dog,Hsq))