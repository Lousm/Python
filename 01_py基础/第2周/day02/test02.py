student = [{'name': '张三', 'age': 18},
           {'name': '小明', 'age': 20},
           {'name': '王五', 'age': 22}]


def fun_max(n):
    return n['age']


max_age = max(student, key=fun_max)
print(max_age)

max_age1 = max(student, key=lambda x: x['age'])
print(max_age1)
