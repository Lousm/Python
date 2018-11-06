import os
from multiprocessing import Process
def run_(name):
     print('子进程运行%s %s'%(name,os.getpid()))

if __name__=='__main__':
    print('父进程%s'%os.getpid())
    p=Process(target=run_,args=('test',))
    print('子进程即将开始')
    p.start()
    p.join()
    print('子进程结束')
