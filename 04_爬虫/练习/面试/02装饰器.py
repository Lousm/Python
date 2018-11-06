# 带参数的装饰器

# a函数就是最原始的装饰器，它的参数是一个函数，然后返回值也是一个函数
def a(func):
    def b(x, y):
        func(x, y)
        print('我是装饰器')

    return b

@a  # 此处加上@a，func()函数就注入了函数a的功能
def func(x, y):
    print('fun')

if __name__ == '__main__':
    f = func  # 这里f被赋值为func，执行f()就是执行func()
    f(3, 4)
