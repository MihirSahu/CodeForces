#!/usr/bin/env python3

import sys


def borrow():
    input1 = sys.stdin.readline().rstrip().split(' ')
    bananaCost = int(input1[0])
    initialMoney = int(input1[1])
    bananasWanted = int(input1[2])

    totalBananaCost = 0

    for i in range(1, bananasWanted + 1):
        totalBananaCost = totalBananaCost + bananaCost
        bananaCost = i * int(input1[0])

    print(totalBananaCost - initialMoney)


borrow()
