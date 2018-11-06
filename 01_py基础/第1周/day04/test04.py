# 判断字符串中的大写，小写，数字的个数
def isCategory(st):
    dzm = 0
    xzm = 0
    shu = 0
    ts = 0
    for i in st:
        a = ord(i)
        if 48 <= a <= 57:
            shu += 1
        elif 65 <= a <= 90:
            dzm += 1
        elif 97 <= a <= 122:
            xzm += 1
        else:
            ts += 1
    print("输入的字符串中大写字母有%d个，小写字母有%d个，数字有%d个,特殊字符有%d个" % (dzm, xzm, shu, ts))

# 判断字符串中的每个字符是否在规定的范围内


def isJudge(st):
    for i in st:
        a = ord(i)
        if not (54 <= a <= 57)and not(66 <= a <= 72)and not(88 <= a <= 90):
            print("输入存在非法字符！！")
            break


isJudge(st=input("请输入字符串："))
isCategory(st=input("请输入字符串："))
