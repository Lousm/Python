import socket,re
from multiprocessing import Process

class Servers(object):
    
    def __init__(self,s):
        self.s=s

    def server(self):
        while True:
            conn,ip_dre=self.s.accept()#等待请求，创建进程
            p=Process(target=self.response,args=(conn,))
            p.start()
            conn.close()

    def response(self,conn):
        resp=conn.recv(1024)
        html_data,num=self.get_path(resp)#响应页面数据
        if num==0:
            a='HTTP/1.1 200 OK\r\n'#响应头（协议）
        else: 
            a='HTTP/1.1 404\r\n'
        b='server:lou\r\n'    #响应头（服务器名称）
        c=html_data            #响应页面
        data=a+b+'\r\n'+c
        conn.send(data.encode('utf-8'))
        conn.close()

    def get_path(self,resp):
        home_path='F:/Python/ProjectPy/0709/第6周/day05/www'
        try:   #正常访问
            path=re.match(r'\w+ (/\S*)',resp.decode("utf-8")).group(1)
            if path=='/':
                path='/index.html'
            f=open(home_path+path,'rb')
            html_data=f.read()
            f.close()
            return(html_data.decode('utf-8'),0)
        except:  #404错误
            f=open(home_path+'/erroy.html','rb')
            html_data=f.read()
            f.close()
            return(html_data.decode('utf-8'),1)
        
def main():
    s=socket.socket()
    s.bind(('',8000))
    s.listen(5)
    ser=Servers(s)
    ser.server()

if __name__=='__main__':
    main()