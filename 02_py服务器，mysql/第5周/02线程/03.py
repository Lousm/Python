import threading
def run_(num):
    print(threading.current_thread().name)
    print(num)

for i in range(5):
    t=threading.Thread(target=run_,args=(i,))
    t.setDaemon(True)
    t.start()
    t.join()