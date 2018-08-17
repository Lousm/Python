def bim(height,weight):
    x=weight/(height**2)
    if x<18.5:
        print('过轻')
    elif x<23.9:
        print('正常')
    elif x<27:
        print('过重')
    elif x<32:
        print('肥胖')
    else:
        print('非常肥胖')

while True:
    height=float(input('请输入身高(m):'))
    weight=float(input('请输入体重(kg):'))
    bim(height,weight)