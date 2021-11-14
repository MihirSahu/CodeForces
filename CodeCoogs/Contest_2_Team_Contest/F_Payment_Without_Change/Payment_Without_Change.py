#!/usr/bin/env python3

import sys


def yes_or_no():

    numCases = int(sys.stdin.readline())

    for i in range(0, numCases):
        break1 = True
        line = sys.stdin.readline().rstrip().split(' ')
        nValueCoins = int(line[0])
        oneValueCoins = int(line[1])
        nValue = int(line[2])
        totalValue = int(line[3])

        while (oneValueCoins != 0) and (break1 == True):
            if (totalValue < oneValueCoins) or ((totalValue % nValue == 0) and (totalValue/nValue > nValueCoins)):
                print("YES")
                break1 = False
            else:
                totalValue -= 1
                oneValueCoins -= 1
            if (oneValueCoins - 1 < 0) and (break1 == True):
                print("NO")


yes_or_no()
