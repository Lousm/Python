num = list(range(1, 101))
c = [num[i:i + 3] for i in range(0, len(num), 3)]
print(c)

a = [i for i in range(100) if i % 2 == 0]
print(a)

b = {key: value for key, value in enumerate(reversed(range(100)))}
print(b)

d = {i for i in range(100)}
print(d)

e = [range(10), range(10, 20)]
f = [j for i in e for j in i]
print(f)
