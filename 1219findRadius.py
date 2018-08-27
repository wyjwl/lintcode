import sys
from math import ceil


def findClosestHeater(heaters, house):
    if heaters is None or len(heaters) == 0:
        return sys.maxsize

    s = 0
    e = len(heaters) - 1

    while s + 1 < e:
        mid = int(s + (e - s) / 2)
        if heaters[mid] == house:
            return 0
        elif heaters[mid] < house:
            s = mid
        else:
            e = mid

    return min(abs(house - heaters[s]),
                        abs(heaters[e] - house))


def findRadius(houses, heaters):
    heaters.sort()

    maxDistance = 0
    for house in houses:
        closestHeaterDistance = findClosestHeater(heaters, house)
        maxDistance = max(maxDistance, closestHeaterDistance)

    return maxDistance


