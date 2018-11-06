import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('10.10.91.184', 8888))

while True:

    data = s.recvfrom(1024)
    print(data[0].decode('gbk'))
    if data != None:
        d = input()
        s.sendto(d.encode('gbk'), ('10.10.91.184', 9999))
    if data[0].decode('gbk') == '0':
        break

s.close()
