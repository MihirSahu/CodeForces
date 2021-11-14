#!/usr/bin/env python3

import sys


def bitpp():

    x = 0
    numStatements = sys.stdin.readline()
    for i in range(0, int(numStatements)):
        line = sys.stdin.readline()
        if '+' in line:
            x += 1
        else:
            x -= 1
    print(x)


bitpp()
