import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('10.10.91.184',8888))
while True:
    data=s.recvfrom(1024)
    print(data[0].decode('utf-8'))
# s.sendto('hello'.decode('utf-8'),('10.10.91.184',6666))