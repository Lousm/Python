class A():
    def __new__(cls,*args,**kwargs):
        if not hasattr (A,'instance'):
            print("没有")
            cls.instance=super().__new__(cls)
        # return super().__new__(cls)
        return cls.instance
    def __init__ (self ,name):
        self.name=name
        print("调用init方法")

a=A('小明')
b=A('小红')
print(a.name)
print(b.name)
print(a is b)