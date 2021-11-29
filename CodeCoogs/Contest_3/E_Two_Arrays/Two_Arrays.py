import sys

def transform():
    numCases = int(sys.stdin.readline().strip())

    for case in range(0, numCases):
        size = int(sys.stdin.readline().strip())
        array1 = sys.stdin.readline().split(' ')
        array2 = sys.stdin.readline().split(' ')

        if array1 == array2:
            print("YES")
            break


# Testing
transform()