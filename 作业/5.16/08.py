import random


def isDaXiao():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    if dice1+dice2+dice3 > 10:
        return '1'
    else:
        return '0'


def user():
    gold = 100
    while True:
        if gold > 0:
            size = input("请输入猜的大小(0:小 1：大)：")
            a = isDaXiao()
            if size == a:
                gold += 10
                print("恭喜你猜对了！金币+10,当前金币余额为:%d" % gold)
            else:
                gold -= 10
                print("很遗憾猜错了！金币-10,当前金币余额为:%d" % gold)
        else:
            print("剩余金币为0，游戏结束")
            exit(0)


user()
