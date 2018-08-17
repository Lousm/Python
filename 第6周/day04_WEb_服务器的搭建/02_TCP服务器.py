import socket
from multiprocessing import Process

def server(s):
    while True:
        conn, ip_dre = s.accept()
        p = Process(target=clien, args=(conn,))
        p.start()
        p.join()
        conn.close()

def clien(conn):
    conn.recv(2048)
    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_header = "Server : fuwuqi\r\n"
    response_body = "hello world"
    datas = response_start_line + response_header + "\r\n" + response_body
    conn.send(datas.encode('utf-8'))
    conn.close()

def main():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('', 8000))
    s.listen(500)
    server(s)

if __name__ == '__main__':
    main()