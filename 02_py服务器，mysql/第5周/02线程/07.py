import threading
local=threading.local()#local相当于ThreadLocal的一个对象，全局变量
                        #每个线程都可以读取local但互不影响
                        
def funcname():
    a_=local.a
    print(a_,threading.current_thread().name)
def run(num):
    local.a=num #a是local的属性，给该属性赋值
    funcname()

t1=threading.Thread(target=run,args=('zhang',))
t2=threading.Thread(target=run,args=('li',))
t1.start()
t2.start()
t1.join()
t2.join()


