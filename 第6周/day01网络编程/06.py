import socket
dress=('10.10.91.184',6666)
s=socket.socket()
s.bind(dress)
#服务器
#开始TCP监听
s.listen(5)
while True:
    print('服务器启动...')

    # 等待链接,阻塞，直到渠道链接 conn打开一个新的对象专门给当前链接的客户端 ip_dre是ip地址
    #其中conn是新的套接字对象，可以用来接收和发送数据。ip_dre是连接客户端的地址。
    conn,ip_dre=s.accept()
    print('客户端地址：%s'%str(ip_dre))

    # 获取客户端请求数据
    data=conn.recv(1024)

    # 打印客户端提交的数据
    print(data.decode('gbk'))
    
    # 向对方发送数据
    conn.send(bytes('我是服务器','gbk'))
    conn.close()