class People(object):
    __getduix=None
    def __new__(cls):
        if cls.__getduix==None:
            cls.__getduix=super().__new__(cls)
        return cls.__getduix
    def __init__ (self ):
        pass
    def say (self):
        print(1111)

p=People()
p.say()
print(id(p))

o=People()
print(id(o))