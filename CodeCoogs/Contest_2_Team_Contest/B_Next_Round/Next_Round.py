#!/usr/bin/env python3

import sys


def nextRound():
    firstLine = sys.stdin.readline().rstrip().split(' ')
    n = int(firstLine[0])
    k = int(firstLine[1])
    scores = sys.stdin.readline().rstrip().split(' ')
    numPassed = 0

    for item in scores:
        if int(item) <= 0:
            pass
        elif int(item) >= int(scores[k]):
            numPassed += 1

    print(numPassed)

nextRound()
