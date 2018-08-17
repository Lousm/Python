import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.sina.com.cn', 80))
print(s)

s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
buff = []
while True:
    d = s.recv(1000)
    if d:
        buff.append(d)
    else:
        break
data = b''.join(buff)
s.close()

heard, html = data.split(b'\r\n\r\n', 1)

with open('sina.html', 'wb') as f:
    f.write(html)
