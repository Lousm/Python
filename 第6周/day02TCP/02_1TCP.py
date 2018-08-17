import socket,threading,time
#服务端

dress=('10.10.91.184',5555)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(dress)
s.listen(102)

def wait():
    while True: #阻塞，每得到一个新的连接，就创建两个线程。一个接收客户端发来的数据，一个给客户端发送数据
        try:
            conn,ip_dre=s.accept()
        except :
            print('断开连接')
        t1=threading.Thread(target=asd,args=(conn,ip_dre))
        t2=threading.Thread(target=qwe,args=(conn,ip_dre))
        t1.start()
        t2.start()
        # conn.close()#把当前创建的conn关闭，但是线程里的conn还存在 （进程中可以用，线程不可以）

def asd(conn,ip_dre):
    while True:
        try:
            data=conn.recv(1024)
            conn.send('sad'.encode('gbk'))#如果客户端断开连接，则conn不存在，这里报错，然后退出线程
            print('客户端IP',ip_dre)
            print(data.decode('gbk'))
        except :
            print('%s已断开连接'%str(ip_dre))
            break

def qwe(conn,ip_dre):
    while True:
        try:
            data=input()
            conn.send(data.encode('gbk'))
        except :
            print('%s已断开连接'%str(ip_dre))
            break

def main():
    wait()

if __name__=='__main__':
    main()