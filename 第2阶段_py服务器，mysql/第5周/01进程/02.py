from multiprocessing import Pool
import os,time,random
def run_(num):
    print('运行的任务 %s %s'%(num,os.getpid()))

if __name__=='__main__':
    print('父进程 %s'%os.getpid())
    p=Pool(3)
    for i in range(101):
        p.apply_async(run_,(i,))
    print('等待所有子进程完成')
    p.close()
    p.join()
    print('所有子进程完成')