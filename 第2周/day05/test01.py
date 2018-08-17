class Student():
    @property
    def age (self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value,int):
            value=0
        self.__age=value

stu=Student()
stu.age='asda'
print('年龄',stu.age)