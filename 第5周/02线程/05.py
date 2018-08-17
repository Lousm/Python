import threading
class Xc (threading.Thread):
    def __init__ (self ,a):
        super().__init__()
        self.a=a
    def run (self):
        for i in range(self.a):
            print(i)
m=Xc(10)
m.start()  #start 运行的是run方法