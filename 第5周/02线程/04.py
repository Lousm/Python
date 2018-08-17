from multiprocessing import Pool, Process
import threading
import time
num = 0
count = 0
f=open('第5周02.04.txt','a',encoding='utf-8')
def zjc():
    for i in range(30000):
        t1 = threading.Thread(target=zxc, args=(5,))
        t2 = threading.Thread(target=zxc, args=(8,))
        t1.start()
        t2.start()

def zxc(n):
    for i in range(10000):
        change_(n)

    # print(threading.current_thread().name)

def change_(n):
    global num, count
    num += n
    num -= n
    count += 1
    f.write(str(count)+' ')

if __name__ == '__main__':
    start_time = time.time()
    p = Pool()
    for i in range(10):
        p.apply_async(zjc)
    p.close()
    p.join()
    print('%2f' % (time.time()-start_time))
    print(num)
    print(count)
    f.close()