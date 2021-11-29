import sys

def modIt():
    numCases = int(sys.stdin.readline().strip())

    for case in range(numCases):
        given = sys.stdin.readline().strip().split(' ')
        x = int(given[0])
        y = int(given[1])

        for i in range(1, 2*pow(10, 8)):
            if i % x == y % i:
                print(i)
                break


# Testing
modIt()