import socket #服务端
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('10.10.91.184',8888))#自己的主机和开启的端口
while True:
    data=s.recvfrom(1024)#接收到的数据
    print(data[0].decode('gbk'))
    if data[0].decode('gbk')=='0':
        break
     
s.close()