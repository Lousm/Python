str1="abcdef"
for i in str1:
    print(i)

print(str1[1:3])
print(str1[:])
print(str1[:-1])

str2="a,b,c,d,e"
list1=str2.split(",")
print(list1)

print(",".join(list1))

print(1111)
print(str1[::2])
print(str1[0:4:2])
print(str1[5:0:-1])

print(str1.find("cd"))
print(str1.count("a"))

print(str1.upper())
print(str1.startswith("a"))
print(str1.startswith("k"))
print(str1.capitalize())

list1.append('g')
print(list1*3)
print(max(list1))
print(min(list1))
print(list1.reverse())
print(list1)

list2=[5,9,65,85,42,95,78,66]
# list2.sort()
list2.sort(reverse=True)
print(list2)