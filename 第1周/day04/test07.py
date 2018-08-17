a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
sum = 0
for i in a:
    if i % 2 == 1:
        sum += i

print(sum)

j = 0
sum1 = 0
while j < len(a):
    if a[j] % 2 == 1:
        sum1 += a[j]
    j += 1
print(sum1)
