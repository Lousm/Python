import threading
def run_():
    print(threading.current_thread().name)
    for i in range(1,5):
        print(threading.current_thread().name,i)

print(threading.current_thread().name)
t=threading.Thread(target=run_)
t.start()
t.join()
print(t.getName()) 