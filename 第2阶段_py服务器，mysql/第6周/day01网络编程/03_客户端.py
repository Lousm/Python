import socket,threading

def a1(s,dress1):
    while True:
        data=input()
        s.sendto(data.encode('gbk'),dress1)

def a2(s,dress2):
    s.bind(dress2)
    while True:
        data=s.recvfrom(1024)
        print(data[0].decode('gbk'))

def main():
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    dress1=('10.10.91.184',9999)
    dress2=('10.10.91.184',8888)
    t1=threading.Thread(target=a1,args=(s,dress1))
    t2=threading.Thread(target=a2,args=(s,dress2))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    s.close()

if __name__=='__main__':
    main()