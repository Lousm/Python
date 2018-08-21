class A():
    def __init__ (self ,name,age):
        self.age=age
        self.name=name
    def __add__(self, other):
        return self.age+other.age

    def __len__ (self):
        return len(self.name)

a=A('zhang',15)
b=A('lisi',3)
print(a+b)
print(len(a))