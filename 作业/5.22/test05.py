def a(f1, f2):
    lis = []
    f = open(f2, 'w', encoding='utf-8')
    with open(f1, 'r', encoding='utf-8') as file:
        for i in file:
            for j in i:
                if not('0' <= j <= '9')and j != ' ':
                    f.write(j)
    f.close()

a('5.22.05.1.txt', '5.22.05.2.txt')
