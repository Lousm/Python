class Login(object):
    def __init__(self, path):
        self.path = path
        self.keys=[]
        self.values=[]
        with open(self.path, 'r', encoding='utf-8') as fil:
            self.data = eval(fil.readline())
            self.keys=self.data.keys()
            self.values=self.data.values()


    def log (self):
        self.uname=input('请输入用户名')
        while True:
            if self.uname not in self.keys:
                self.uname=input('用户名不存在！请重新输入：')
            else:
                break
        
        self.upassword=input('请输入密码：')
        self.password=list(self.data.values())[list(self.data.keys()).index(self.uname)]
        while True:
            if self.upassword != self.password:
                self.upassword=input('密码错误！请重新输入：')
            else:
                break
        print('%s登录成功!'%self.uname)
