import socket
import threading

class Client(object):
    def __init__(self, s, dress):
        self.s = s
        self.dress = dress

    def a(self):
        while True:
            data = input()
            self.s.sendto(data.encode('gbk'), self.dress)

class Server(object):
    def __init__(self, s, dress):
        self.s = s
        self.dress = dress

    def a(self):
        while True:
            data = self.s.recvfrom(1024)
            print(data[0].decode('gbk'), self.dress)

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dress1 = ('127.0.0.1', 6666)
    dress2 = ('127.0.0.1', 5555)
    # print(s.getsockname())    
    s.bind(dress2)
    cli = Client(s, dress1)
    ser = Server(s, dress2)
    t1 = threading.Thread(target=cli.a)
    t2 = threading.Thread(target=ser.a)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    main()
