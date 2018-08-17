class File():
    def __init__(self, path):
        self.path = path
        with open(self.path, 'r', encoding='utf-8') as fil:
            self.contents = eval(fil.readline())

    def wri(self):
        with open(self.path, 'w', encoding='utf-8') as fil:
            fil.write(str(self.contents))

    def tj(self):
        for i in range(3):
            data = int(input('请输入第%d，个数字' % (i+1)))
            self.contents.append(data)


fi = File('data.txt')
fi.tj()
fi.wri()
