import socket
from threading import Thread

class Udp(object):
    def __init__ (self ,s):
        self.s=s
    
    def a(self):
        p1=Thread(target=self.fs)
        p2=Thread(target=self.js)
        p1.start()
        p2.start()

    def fs(self):
        while True:
            data=input('请输入：')
            self.s.sendto(data.encode('utf-8'),('10.10.91.230',9999))
    
    def js(self):
        while True:
            data=self.s.recvfrom(1024)
            print(data[0].decode('utf-8'))

def main():
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind(('10.10.91.184',8888))
    udp=Udp(s)
    udp.a()

if __name__ == '__main__':
    main()