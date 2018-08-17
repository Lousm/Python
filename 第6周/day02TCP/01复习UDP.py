import socket,threading
class Khd(object):
    def __init__ (self ,s,dress):
        self.s=s
        self.dress=dress

    def a (self):
        while True:
            data=input()
            self.s.sendto(data.encode('gbk'),self.dress)

class Fwd(object):
    def __init__ (self ,s,dress):
        self.s=s
        self.dress=dress

    def a (self):
        while True:
            data=self.s.recv(1024)
            print(data.decode('gbk'))

def main():
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    dress1=('10.10.91.184',8888)
    dress2=('10.10.91.184',9999)
    k=Khd(s,dress1)
    f=Fwd(s,dress2)
    s.bind(dress2)
    t1=threading.Thread(target=k.a)
    t2=threading.Thread(target=f.a)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__=='__main__':
    main()