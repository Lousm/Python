import collections
c=collections.Counter()
for a in 'dsjfhshjfesdfjkdhjk':
    c[a]=c[a]+1
print(c)

# Counter({'j': 4, 'd': 3, 's': 3, 'f': 3, 'h': 3, 'k': 2, 'e': 1})