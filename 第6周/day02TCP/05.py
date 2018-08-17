from socket import *
from threading import Thread
import time
tcp_server_socket = socket(AF_INET,SOCK_STREAM)
address = ('10.10.91.184',5555)
tcp_server_socket.bind(address)
tcp_server_socket.listen(6)
def get_message(new_socket,new_address,l):
    while True:
        try:
            message = new_socket.recv(1024)
            strings = new_address[0] +' '+ str(new_address[1])+' '+\
                      time.strftime('%Y-%m-%d %H:%M:%S')+':'+'\r\n'+message.decode('gbk')+'\r\n'
            l.append(strings)
            print(strings)
            new_socket.send(strings.encode('gbk'))
        except:
            print(new_address[0],new_address[1], '下线了！')
            break

def send_message(new_socket,new_address):
    while True:
        try:
            print(new_address)
            strings = input() + '\r\n'
            new_socket.send(strings.encode('gbk'))
        except(ConnectionResetError):
            print(new_address,'下线了！')
            break

l = []
while True:
    new_socket,new_address = tcp_server_socket.accept()
    print(new_address[0],new_address[1],'上线了！')
    # t_1 = Thread(target=send_message,args=(new_socket,new_address))
    t_2 = Thread(target=get_message,args=(new_socket,new_address,l))
    # t_1.start()
    t_2.start()

    # new_socket.close()
