#!/usr/bin/env python3

"""
A. Mr. Skeleton
time limit per test
1 second
memory limit per test
256 megabytes
input
standard input
output
standard output

Mr. Skeleton is a groovy guy. He has N
bones. Wait, wait a minute, he thought he had N bones. 1, 2, 3, 4...aw crap, not again. He swears he had N

, they were just here!

Well, it's hard being a skeleton, and sometimes you just have to pick yourself up off the ground, even if that means literally. As in literally going back and picking up pieces of your body where they fell off and you forgot them.

Help Mr. Skeleton figure out which bones he's missing this time. Given that Mr. Skeleton normally has bones 1
through N and now he only has some subset of those bones still attached, H

of them to be precise, compute the list of lost bones that Mr. Skeleton has left to find!
Input

The first line contains two integers: N
(1≤N≤105), the total number of bones that Mr. Skeleton normally has when he has all of his bones, and H (1≤H≤N), the number of bones he currently has on him. The next H lines each contain the name bi (1≤bi≤N

) of one of Mr. Skeleton's unique bones that he has verified is currently in his possession (i.e. not missing).
Output

Print out the numeric name of each bone that Mr. Skeleton is still missing. The bone names should be printed out on separate lines, in order from least to greatest number.
Example
Input

9 4
2
1
7
5

Output

3
4
6
8
9
"""

import sys

def missing_bones():

    inputList = []
    line1 = sys.stdin.readline()
    inputList.append(line1.rstrip())
    totalBones = inputList[0][0]
    currentBones = inputList[0][-1]
    for i in range(1, int(currentBones) + 1):
        line = sys.stdin.readline()
        inputList.append(int(line.rstrip()))

    print("")
    for i in range(1, int(totalBones) + 1):
        if i not in inputList:
            print(i)

# Testing
missing_bones()
