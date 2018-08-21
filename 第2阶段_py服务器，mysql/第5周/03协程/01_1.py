import greenlet,time
# print(greenlet)

def a1():
    while True:
        print(11111111)
        g2.switch()
        g3.switch()
        # time.sleep(1)

def a2():
    while True:
        print(22222222)
        g1.switch()
        g3.switch()
        print("----------")
        # time.sleep(1)

def a3():
    while True:
        print(33333333)
        g1.switch()
        g2.switch()
        print('==============')
        # time.sleep(1)




def main():
    g1.switch()
if __name__=='__main__':
    g1=greenlet.greenlet(a1)
    g2=greenlet.greenlet(a2)
    g3=greenlet.greenlet(a3)
    main()