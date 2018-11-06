import matplotlib.pyplot as plt
import numpy

x = numpy.arange(0, 3 * numpy.pi, 0.1)
y_sin = numpy.sin(x)
y_cos = numpy.cos(x)
y2 = x ** 2

p = plt.figure(figsize=(10, 9), dpi=100)

# 正弦
p.add_subplot(2, 2, 1)
plt.plot(x, y_sin)
plt.legend(['y=sin(x)'])

# 余弦
p.add_subplot(2, 2, 2)
plt.plot(x, y_cos, 'r')
plt.legend(['y=cos(x)'])

# 圆
p.add_subplot(2, 2, 3)
plt.plot(y_sin, y_cos, 'y')
plt.legend(['x^2+y^2=1'])

# x**2
p.add_subplot(2, 2, 4)
plt.plot(x, y2, 'g')
plt.legend(['y=x^2'])

# 显示
plt.show()
