import greenlet
def a1():
    while True:
        print(11111111)
        g2.switch()
        print(22222222)
def a2():
    while True:
        print(33333333)
        g1.switch()
        print(44444444)
def main():
    g1.switch()
if __name__=='__main__':
    g1=greenlet.greenlet(a1)
    g2=greenlet.greenlet(a2)
    main()