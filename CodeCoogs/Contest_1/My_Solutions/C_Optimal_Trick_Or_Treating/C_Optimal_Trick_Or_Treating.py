"""
C. Optimal Trick or Treating
time limit per test
1 second
memory limit per test
256 megabytes
input
standard input
output
standard output

Little Timmy is going trick or treating this year, but has decided that he will only look for his favorite kind of candy: Chuckles bars. Unfortunately, Alice has bought up all of the Chuckles bars in the neighborhood and using them to trade for other candies, so Timmy must find the candies that Alice is looking for and trade them in for Chuckles bars. Alice has posted n

types of trades that she is willing to make, where a trade consists of a type of candy and how many Chuckles bars Alice is willing to give for one piece of that type of candy.

Little Timmy has done extensive research and discovered what candies and amounts each of the h
houses in his neighborhood is going to be giving out. When Little Timmy goes to a particular house, he can take all of the candy that the house is giving out. However, he only has time to visit k

different houses before the night ends. Given the candies that each house gives out and the deals Alice is willing to make, what is the maximum amount of Chuckles bars that Little Timmy can end up getting?
Input

The first line of the input will consist of a single integer n
(1≤n≤200), which gives the number of deals that Alice is willing to make. The next n lines of the input will consist of a string si made of only alphanumeric characters (1≤|si|≤15) and an integer vi (1≤vi≤100), which indicates that Alice is willing to give vi Chuckles bars for a single candy with the name si. The next line of the input will consist of two integers h and k (1≤k≤h≤200), which gives the number of houses in Timmy's neighborhood and the number of houses that he can visit. The next lines of the input consist of h house-descriptions, which consist of a single integer ci (1≤ci≤n) giving the number of types of candies that house i is giving out, followed by ci lines that each consist of one of the n types of candies that Alice is willing to send and an integer mj (1≤mj≤100) that gives the number of candies of that type that house i

is giving out.
Output

Output a single integer and new line that gives the maximum number of Chuckles bars that Little Timmy can end up collecting.
Example
Input
Copy

3
LactoseyWay 2
Twicks 3
DigDog 5
2 1
2
LactoseyWay 3
Twicks 1
1
DigDog 2

Output
Copy

10
"""

import sys


def max_candy():
    aliceMenu = []
    numMenu = int(sys.stdin.readline().rstrip())

    for i in range(0, numMenu):
        aliceMenu.append(sys.stdin.readline().rstrip())

    tempString = sys.stdin.readline().rstrip()
    numHouses = int(tempString[0])
    canVisit = int(tempString[2])

    houseCandyList = []

    for i in range(0, numHouses):
        numHouseCandyType = int(sys.stdin.readline().rstrip())
        currentTotalHouseCandy = 0

        for j in range(0, numHouseCandyType):
            temp = sys.stdin.readline().rstrip()
            for k in aliceMenu:
                if temp[:temp.index(' ')] == k[:temp.index(' ')]:
                    currentTotalHouseCandy = currentTotalHouseCandy + (int(temp[temp.index(' ') + 1:])*int(k[temp.index(' ') + 1:]))
                    break

        houseCandyList.append(currentTotalHouseCandy)

    print('')
    print(houseCandyList)

    totalCandy = 0
    for i in range(0, canVisit):
        totalCandy = totalCandy + max(houseCandyList)
        houseCandyList.remove(max(houseCandyList))

    print(totalCandy)

# Testing
max_candy()
