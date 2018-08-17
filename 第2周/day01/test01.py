def hsj():
    for i in range(1, 8):
        for j in range(1,(7-i+1)):
            print(end=' ')
        for j in range(1, 2*i-1+1):
            if j == 1 or j == 2*i-1 or i == 7:
                print("*", end='')
            else:
                print(end=' ')
        print()


hsj()

def whsj():
    i=1
    while i<8:
        j=1
        while j<=7-i:
            print(end=' ')
            j+=1
        j=1
        while j<2*i-1+1:
            if j==1 or j==2*i-1 or i==7:
                print('*',end='')
            else:
                print(end=' ')
            j+=1
        print()
        i+=1
whsj()

def add(a,b):
    c=a+b