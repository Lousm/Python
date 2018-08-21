import socket
s=socket.socket()
dress=('10.10.91.184',6666)
s.bind(dress)
s.listen(5)
while True:
    conn,ip_dre=s.accept()
    conn.send('你好， 我是服务器'.encode('gbk'))
    data=conn.recv(1024)
    print(data.decode('gbk'))