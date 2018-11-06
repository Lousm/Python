import threading,time
num = 0

def change_(n):
    global num
    num +=n
    num -=n

def run_(n):
    for i in range(1000000):
        change_(n)
start_time=time.time()
t1 = threading.Thread(target=run_, args=(5,))
t2 = threading.Thread(target=run_, args=(8,))
t1.start()
t2.start()
print('%2f'%(time.time()-start_time))
print(num)