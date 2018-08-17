class People():
    tax=0
    def __init__ (self ,name,age,work,salary,energy=100):
        if 0<=energy<=100:
            self.__energy=energy
        else:
            raise Exception('精力值应在0到100之间')
        self.name=name
        self.age=age
        self.work=work
        self.salary=salary
        
    
    def eat (self,money):
        self.__energy+=10
        self.salary-=money
    def say (self):
        print('我是%s,今年%d，我的工作是%s，工资是%d，还有%d精力'%(self.name,self.age,self.work,self.salary,self.__energy))
    def working (self):
        self.tax+=self.salary*0.2
        self.__energy-=30
    def sleep (self):
        self.__energy+=60
    def get_energy (self):
        num=self.__energy
        return num

class Woman(People):
    def shping (self,money):
        self.salary-=money
    
class Man(People):
    def say (self):
        print('我是%s,今年%d，我的工作是%s，工资是%d，还有%d精力'%(self.name,self.age,self.work,self.salary,self.get_energy()))
    
man=Man('张三',22,'程序员',15000)
man.say()