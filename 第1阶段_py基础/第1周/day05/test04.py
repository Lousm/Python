# 石头剪刀布游戏
import random


def sjb():
    while True:
        n = int(input("请输入0-2：0:石头 1：剪刀 2：布"))
        if n == 3:
            exit(0)
        print("您出的是  :", end='')
        gesture(n)
        y = random.randint(0, 2)
        print
        print("对手出的是:", end='')
        gesture(y)
        judge(n, y)


def gesture(n):
    if n == 0:
        print("石头")
    elif n == 1:
        print("剪刀")
    elif n == 2:
        print("布")


def judge(n, y):
    if n == y:
        print("平局！")
    elif (n == 0 and y == 1)or (n == 1 and y == 2)or (n == 2 and y == 0):
        print("您胜！")
    else:
        print("对方胜！！")


sjb()
