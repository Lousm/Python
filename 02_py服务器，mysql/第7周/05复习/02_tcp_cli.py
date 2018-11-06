import socket
from threading import Thread
def cli(s):
    t1=Thread(target=fs,args=(s,))
    t2=Thread(target=js,args=(s,))
    t1.start()
    t2.start()

def fs(s):
    while True:
        data=input('请输入：')
        s.send(data.encode('utf-8'))

def js(s):
    while True:
        data=s.recvfrom(1024)
        print(data[0].decode('utf-8'))

def main():
    s=socket.socket()
    s.connect(('10.10.91.184',8888))
    cli(s)

if __name__ == '__main__':
    main()