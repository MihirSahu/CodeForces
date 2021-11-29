
import sys

def subtract():
    given = sys.stdin.readline().split(' ')
    num = list(given[0])
    k = int(given[1])

    for i in range(0, k):
        if int(num[-1]) != 0:
            num[-1] = str(int(num[-1]) - 1)
        else:
            num = list(str(int(int(''.join(num)) / 10)))
    
    print(int(''.join(num)))


# Testing
subtract()