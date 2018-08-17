import os
from multiprocessing import Process,Queue
from queue import LifoQueue
def run1(q):
    li=[1,2,3,4]
    for i in li:
        q.put(i)
def run2(q):
    while True:
        if not q.empty():
            print(q.get())
        else:
            break
if __name__=='__main__':
    print('父进程%d'%os.getpid())
    q=LifoQueue()
    # q=Queue()
    p1=Process(target=run1,args=(q,))
    p1.start()
    p1.join()

    p2=Process(target=run2,args=(q,))
    p2.start()
    p2.join()