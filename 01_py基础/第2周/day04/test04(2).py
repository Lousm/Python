import os
class File():
    
    def __init__(self, path):
        self.path = path
        
        with open(self.path, 'r', encoding='utf-8') as fil:
            self.a = eval(fil.readline())

    def wir(self):
        with open(self.path, 'w', encoding='utf-8') as fil:
            fil.write(str(self.a))

    def tj(self):
        for i in range(1, 4):
            data = int(input('请输入第%d个数：' % i))
            self.a.append(data)

print(os.getcwd())
fi = File('data.txt')
fi.tj()
fi.wir()
