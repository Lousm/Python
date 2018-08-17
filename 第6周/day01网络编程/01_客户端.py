import socket  #客户端
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  #建立一个UDP套接字
while True:
    data=input()#要发送的字符
    s.sendto(data.encode('gbk'),('10.10.91.184',9999))#发送给目标主机
    if data=='0':
        break

s.close()

