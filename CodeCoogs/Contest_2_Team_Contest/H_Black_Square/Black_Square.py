#!/usr/bin/env python3

import sys


def calories_wasted():
    calories = sys.stdin.readline().rstrip().split(' ')
    rounds = list(sys.stdin.readline().rstrip())
    caloriesWasted = 0

    for idx, i in enumerate(rounds):
        caloriesWasted += int(calories[int(i) - 1])

    print(caloriesWasted)


calories_wasted()
