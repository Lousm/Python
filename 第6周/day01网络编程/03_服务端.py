import socket,threading
class Khd (object):#客户端
    def __init__(self, s, dress1):
        self.s = s
        self.dress1 = dress1
    def a1(self):
        while True:
            data = input()
            self.s.sendto(data.encode('gbk'), self.dress1)

class Fwd(object):#服务端
    def __init__(self, s, dress2):
        self.s = s
        self.dress2 = dress2

    def a2(self):
        while True:
            data = self.s.recvfrom(1024)
            print(data[0].decode('gbk'))

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dress1 = ('10.10.91.184', 9999)
    dress2 = ('10.10.91.184', 8888)
    s.bind(dress2)
    k = Khd(s, dress1)
    f = Fwd(s, dress2)
    t1 = threading.Thread(target=k.a1)
    t1.start()
    t2 = threading.Thread(target=f.a2)
    t2.start()
    s.close()

if __name__ == '__main__':
    main()
