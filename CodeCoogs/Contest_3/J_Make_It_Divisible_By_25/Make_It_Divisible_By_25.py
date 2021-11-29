import sys

def divisible_recursive(count, current):
    for idx, digit in enumerate(current):
        temp = list(current)
        temp.pop(idx)
        count += 1
        if len(temp) == 1:
            if int(temp[0]) % 25 == 0:
                break
        elif int(''.join(temp)) % 25 == 0:
            break
        else:
            divisible_recursive(count, temp)

def divisible():
    numCases = int(sys.stdin.readline().strip())
    count = 0

    for number in range(0, numCases):
        current = list(str(sys.stdin.readline().strip()))
        if int(''.join(current)) % 25 == 0:
            print(0)
            continue
        for idx, digit in enumerate(current):
            count = 0
            temp = list(current)
            temp.pop(idx)
            count += 1
            if len(temp) == 1:
                if int(temp[0]) % 25 == 0:
                    break
            elif int(''.join(temp)) % 25 == 0:
                break
            else:
                divisible_recursive(count, temp)
        print(count) 


# Testing
divisible()