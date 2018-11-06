import numpy

a = numpy.array([1, 2, 3])
print(a)

b = numpy.array([1, 2, 3, 4, 5, 6], ndmin=2)
print(b)

c = numpy.array([1, 2, 3, 4, 5], dtype=complex)
print(c)

print(numpy.dtype(numpy.float))

# 创建结构化数据类型
dt = numpy.dtype([('age', numpy.int8)])
# dt = numpy.dtype([('age', numpy.float)])
print(dt)
# 将创建的数据类型那个应用于数组对象
d = numpy.array([1, 2, 3, 4], dtype=dt)
print(d)
print(d['age'])

# 定义名为student 的结构化数据类型,其中包含字符串字段name 整数字段age 浮点型字段marks
student = numpy.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
print(student)
e = numpy.array([('xiaoming', 18, 44), ('lisi', 21, 55)], dtype=student)
print(e)


#####################数组属性###############
# .shape 这一数组属性返回一个包含数组维度的元组，它也可以用于调整数组大小。


