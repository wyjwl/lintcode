from math import ceil


def findNthDigit(n):
    if n <= 9:
        return n
    base = 9
    digit = 1
    while n - base * digit > 0:
        n -= base*digit
        base *= 10
        digit += 1

    start = base / 9 - 1

    finalNumber = start + ceil(n/digit)

    numStr = str(int(finalNumber))

    return int(numStr[n%digit - 1])





print(findNthDigit(15))


