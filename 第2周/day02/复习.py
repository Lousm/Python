def x(a):
    return a**2
print(x(7))

z = {'name': '张三', 'age': 18}

def y(a):
    return a['age']

print(y(z))

student = [{'name': '张三', 'age': 18},
           {'name': '小明', 'age': 20},
           {'name': '王五', 'age': 22}]

def asd(a):
    return a['age']

max_age=max(student,key=asd)
print(max_age)

max_age1=max(student,key=lambda x: x['age'])
print(max_age1)