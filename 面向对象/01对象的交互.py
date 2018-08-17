class People():
    role = '人类'

    def walk(self):
        print('小明会走路')

    def __init__(self, name, aggressivity, blood_flow):
        self.name = name
        self.aggressivity = aggressivity  # 每一个角色都有自己的攻击力;
        self.blood_flow = blood_flow  # 每一个角色都有自己的血量;

    def attack(self, dog):
        # 人可以攻击狗，这里的狗也是一个对象。
        # 人攻击狗，那么狗的生命值就会根据人的攻击力而下降
        dog.blood_flow -= self.blood_flow


class Dog():
    role = '狗'

    def __init__(self, name, breed, aggressivity, blood_flow):
        self.name=name
        self.breed=breed
        self.aggressivity=aggressivity
        self.blood_flow=blood_flow

    def attack (self,people):
        people.blood_flow-=self.aggressivity


egg = People('小王', 10, 1000)
dog=Dog('A','2哈',10,1000)

# print(People.role)
# print(People.walk) #引用人的走路方法，注意，这里不是在调用
print(egg.role)
print(egg.walk())

dog.attack(egg)
print('人的血量%s'%egg.blood_flow)
