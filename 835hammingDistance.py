def hammingDistance(x, y):
    distance = 0
    if x == y:
        return distance
    while x != 0 or y != 0:
        if x % 2 != y % 2:
            distance += 1
        x = int(x/2)
        y = int(y/2)
    return distance


print(hammingDistance(1,4))