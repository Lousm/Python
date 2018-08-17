import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    data=input()
    s.sendto(data.encode('utf-8'),('10.10.91.184',9999))