import socket,threading
#客户端
class Khd(object):
    def __init__ (self ,s,dress):
        self.s=s
        self.dress=dress
        self.s.connect(dress)
    def fs(self):#客户端发送数据
        while True:
            data=input()
            self.s.send(data.encode('gbk'))

    def js(self):#客户端接收数据
        while True:
            try:
                data=self.s.recv(1024)
                print(data.decode('gbk'))
            except:
                print('数据过大')
            
def main():
    dress=('10.10.91.221',9999)
    s=socket.socket()
    k=Khd(s,dress)
    t1=threading.Thread(target=k.fs)
    t2=threading.Thread(target=k.js)
    t1.start()
    t2.start()

if __name__=='__main__':
    main()