import socket,re,os
from multiprocessing import Process

def server(s):
    while True:
        conn, ip_dre = s.accept()
        p = Process(target=clien, args=(conn,))
        p.start()
        p.join()
        conn.close()

def clien(conn):
    request=conn.recv(1024)
    a=getRequestPath(request)
    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_header = "Server : fuwuqi\r\n"
    response_body = a.decode('utf-8')
    datas = response_start_line + response_header + "\r\n" + response_body
    conn.send(datas.encode('utf-8'))
    conn.close()

def getRequestPath(request):
    home_path=os.getcwd()
    a='F:/Python/ProjectPy/0709/第6周/day04_WEb_服务器的搭建/www'
    request_line=request.splitlines()[0].decode('utf-8')
    path=re.match(r'\w+ (/\S*)',request_line).group(1)
    if path=='/':
        path='/index.html'
    f=open(a+path,'rb') 
    data=f.read()
    f.close()
    print(home_path)
    print(path)
    return(data)

def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('', 8000))
    s.listen(500)
    server(s)

if __name__ == '__main__':
    main()