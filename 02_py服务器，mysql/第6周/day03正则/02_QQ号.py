import re
while True:
    try:
        string=input('请输入QQ号')
        r=re.match('^[1-9]\d{4,9}',string)
        print(r.group())
    except:
        print('请输入正确QQ号')
