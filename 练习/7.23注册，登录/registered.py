class Registered(object):
    def __init__(self, path):
        self.path = path
        self.keys=[]
        with open(self.path, 'r', encoding='utf-8') as fil:
            self.data = eval(fil.readline())
            self.keys=self.data.keys()
            

    def wri(self):
        with open(self.path, 'w', encoding='utf-8') as fil:
            fil.write(str(self.data))

    def add (self):
        self.uname=input('请输入用户名：')
        while True:
            if self.isLegal(self.uname):
                self.uname=input('包含特殊字符！请重新输入：')
            elif self.uname in self.keys:
                print('注册----',type(self.keys))
                self.uname=input('用户名已存在！请重新输入：')
            else:
                break

        self.upassword=input('请输入密码：')
        while True:
            if self.isLegal(self.upassword):
                self.upassword=input('包含特殊字符！请重新输入：')
            else:
                break
        
        self.data[self.uname]=self.upassword
        self.wri()
        print('%s注册成功!'%self.uname)

    def isLegal(self,s):
        for i in s:
            if not('a' <= i <= 'z')and not('A' <= i <= 'Z') and i != '_' and not('0' <= i <= '9'):
                return True

