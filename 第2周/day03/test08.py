class A():
    count = 0

    def __init__(self, name):
        self.name = name
        A.count += 1
        print("第%d个对象，%s" % (A.count, self.name))

    def __del__(self):
        A.count -= 1
        print('%s被释放,还有%d个对象' % (self.name, A.count))


a = A('小明')
b = A('小红')
