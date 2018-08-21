a = [0, 5, 6, 4, 2, 3, 5, 64, 6, 4, 6, 1, 3, 444, 33, 95]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

print(11 in a)
print(11 not in a)

for i in a:
    print(i)
print("----------------")
i=0
while i<len(a):
    print(a[i])
    i+=1

