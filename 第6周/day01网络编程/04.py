import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',8080))
s.listen(5)

conn,address=s.accept()
s.sendall(bytes('asd',encoding='utf-8'))


# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',8080))

print(s.recv(1024),encoding='utf-8')