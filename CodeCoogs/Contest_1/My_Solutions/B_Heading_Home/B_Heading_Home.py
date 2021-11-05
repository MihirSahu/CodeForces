"""
B. Heading Home
time limit per test
1 second
memory limit per test
256 megabytes
input
standard input
output
standard output

Abhinav is far away from his home on Halloween night! He's incredible scared of being attacked by ghosts, so he wants to run home as quick as he can to maximize his chance of making it through the night safely.

We can model Abhinav's position and his home's position as points on a number line as a
and h, respectively. In a single second, Abhinav can move anywhere between 1 and d units. Given a, h, and d

, can you figure out how fast Abhinav can make it back home?
Input

The first line will consist of a single integer T
(1≤T≤1000) consisting of the number of test cases you will need to process. The next T lines each consist of a single test case with 3 space separated integers a, h, d (1≤a,h,d≤105

), which represent Abhinav's position, his home's position, and his max speed.
Output

For each test case, output a single integer giving the minimum amount of time (in seconds) it will take Abhinav to reach his home.
Example
Input
Copy

3
1 5 1
1 5 2
1 5 3

Output
Copy

4
2
2
"""

import sys
import math


def max_time():
    numLines = int(sys.stdin.readline().rstrip())

    print("")
    for i in range(0, numLines):
        line = sys.stdin.readline().rstrip()
        print(math.ceil((int(line[2]) - int(line[0]))/int(line[4])))


# Testing
max_time()
