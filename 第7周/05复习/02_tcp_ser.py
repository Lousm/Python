import socket
from multiprocessing import Process
from threading import Thread
s=socket.socket()
s.bind(('10.10.91.184',6666))
s.listen(5)

def ser(conn,ip_dre):#接收从客户端发来的消息
    while True:
        try:
            data=conn.recv(1024)
            print(data.decode('utf-8'))
        except:
            print('已下线')
            break
    conn.close()
        
def fs(conn,ip_dre):
    while True:
        try:
            data=input('请输入：')
            conn.send(data.encode('utf-8'))
        except:
            print('已下线....')
            break
    conn.close()
        
def main():
    while True:
        conn,ip_dre=s.accept()
        t1=Thread(target=ser,args=(conn,ip_dre))
        t2=Thread(target=fs,args=(conn,ip_dre))
        t1.start()
        t2.start()
    conn.close()

if __name__ == '__main__':
    main()