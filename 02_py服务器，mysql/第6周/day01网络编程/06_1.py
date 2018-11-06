import socket
dress=('10.10.91.184',8888)
s=socket.socket()
#请求连接服务器
s.connect(dress)
#向服务器发送数据
s.send('你好，服务器'.encode('gbk'))
while True:
    #接受数据
    data=s.recv(1024)
    print(data.decode('gbk'))
s.close()