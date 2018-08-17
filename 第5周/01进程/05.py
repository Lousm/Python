from multiprocessing import Process
import os
class Zjc(Process):
    def run (self):
        print('子进程%d'%os.getpid())

def aaa(num):
    print('aaa')
if __name__=='__main__':
    z=Zjc(target=Zjc.run,args=(1,))
    a=Zjc(target=aaa,args=(1,))
    z.start()
    a.start()