import socket,greenlet
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('10.10.91.184', 8888))

def fs():
    g2.switch()
    data = s.recvfrom(1024)
    print(data[0].decode('gbk'))
    

def js():
    d = input('请输入：')
    g1.switch()
    s.sendto(d.encode('gbk'), ('10.10.91.184', 9999))
    

def main():
    g1.switch()
if __name__=='__main__':
    g1=greenlet.greenlet(fs)
    g2=greenlet.greenlet(js)
    main()

s.close()