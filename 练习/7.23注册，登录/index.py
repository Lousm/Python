import registered
import login

re=registered.Registered('7.23注册.登录.txt')
lo=login.Login('7.23注册.登录.txt')
def star ():
    while True:
        print('================================管理系统==============================')
        oper = input("请输入你要进行的操作：\n\t1.登录.\n\t2.注册.\n\t0.退出.\n")
        print('=====================================================================')
        if oper == '1':
            lo.log()
        elif oper == '2':
            re.add()
        else:
            print('程序退出')
            exit(0)

star()