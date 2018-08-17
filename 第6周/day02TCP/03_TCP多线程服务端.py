import socket,threading,time
#服务端

dress=('10.10.91.184',9999)
s=socket.socket()
s.bind(dress)
s.listen(102)
def js():
    while True:
        conn,ip_dre=s.accept()
        t=threading.Thread(target=asd,args=(conn,ip_dre))
        print(threading.current_thread().name)
        t.start()
    conn.close()

def asd(conn,ip_dre):
    while True:
        data=conn.recv(99999)
        print('客户端IP',ip_dre)
        print(data.decode('gbk'))
        conn.send(ip_dre[0].encode('gbk'))
        conn.send(data)
        conn.send(' 你好 ，我是服务器'.encode('gbk'))
    
def main():
    js()

if __name__=='__main__':
    main()