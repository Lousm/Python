name=['zhangsan']
def func(n):
    name=n
    print(name)
    def func1():
        nonlocal name
        name='xiaohong'
        print(name)
    func1()
    print(name)

func('lisi')