
import sys

def makeEven():
    numCases = int(sys.stdin.readline().strip())
    count = 0

    for number in range(0, numCases):
        current = list(str(sys.stdin.readline().strip()))

        if current % 2 == 0:
            break
        else:
            for idx, digit in enumerate(current):
                if int(digit) % 2 == 0:
                    temp = current[:idx + 1].reverse()
                    temp.append(current[idx + 1:])
    
    return count

# Testing
makeEven()