#!/usr/bin/env python3

"""
King Boo has N

ghosts standing in a line. This year, they decide that they want to go ghosting and treating. While trick-or-treating is relatively simple for humans, for ghosts, instead they need to scare people and steal their candy when they're terrified. But, being ghosts, they're kind of lazy, and so Boo has decided a system where only one ghost will go out and do this task this year so everyone can have some candy.

Every single ghost has been a ghost for a certain number of whole number years. Boo has decided to repeatedly pick out two ghosts with different "ages" that are adjacent to each other in the line, and if one of them has been a ghost longer than the other, the younger ghost will step out of line and is no long in the running to be a ghost-or-treater. However, matches are tiring to the participants involved, so the ghost that stays in line will effectively age a year. This process repeats until all Boo can no longer select two ghosts, and Boo will declare the remaining ghost(s) the "winner(s)" to go ghost-or-treating.

Given the ages of each of the ghosts in order, is there a way that Boo can set up the matches such that only one ghost will have to go ghost-or-treating (in other words, only one ghost will be remaining in line)?
Input

The first line will contain N
(1≤N≤104)

, the number of ghosts.

The next N
lines will each contain the age X (1≤X≤109)

of a ghost in years.
Output

Output YES if it is possible to send out exactly one ghost, and NO if not.
Examples
Input

5
5
3
4
4
5

Output

YES

Input

3
1
1
1

Output

NO

Input

5
4
4
3
4
4

Output
Copy

YES

Note

In the first sample case, the matchups can be the following:

1st ghost v.s. 2nd ghost, 1st ghost stays in line and is now 6 years old

1st ghost v.s. 3rd ghost, 1st ghost stays in line and is now 7 years old

4th ghost v.s. 5th ghost, 5th ghost stays in line and is now 6 years old

1st ghost v.s. 5th ghost, 1st ghost stays in line and no one else is left

Note that the 1st ghost and 3rd ghost are adjacent after the 2nd ghost steps out of line when the first matchup completes.
"""

import sys


def ghostOrTreat():

    ghostList = []
    numGhosts = int(sys.stdin.readline())

    for i in range(0, numGhosts):
        ghostList.append(int(sys.stdin.readline()))

    idx = 0
    while idx < len(ghostList) - 1:
        if (ghostList[idx] > ghostList[idx + 1]):
            ghostList[idx] = ghostList[idx] + 1
            ghostList.pop(idx + 1)
            idx -= 1
            print(idx)
        elif (ghostList[idx] < ghostList[idx + 1]):
            ghostList[idx + 1] = ghostList[idx + 1] + 1
            ghostList.pop(idx)
            idx -= 1
            print(idx)
        print(ghostList)

    if len(ghostList) == 1:
        return True;
    return False

# Testing
print(ghostOrTreat())
