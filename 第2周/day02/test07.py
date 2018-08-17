def cop(n):
    f = open(n, 'r', encoding='utf-8')
    f1 = open('F:\\Python\\ProjectPy\\0709\\第2周\\day02\\2.txt', 'a', encoding='utf-8')
    for i in f:
        for j in i:
            if j !='0':
                f1.write(j)
    f1.close()
    f.close()

cop('F:\\Python\\ProjectPy\\0709\\第2周\\day02\\1.txt')