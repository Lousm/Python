import threading,time

local=threading.local()

def change_(n):
    local.num +=n
    local.num -=n
def run_(n):
    local.num=0
    for i in range(1000000):
        change_(n)
    print(local.num)
start_time=time.time()
t1 = threading.Thread(target=run_, args=(5,))
t2 = threading.Thread(target=run_, args=(8,))
t1.start()
t2.start()
print('%2f'%(time.time()-start_time))
