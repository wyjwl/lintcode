def askForCoolingTime(arr, n):
    time = 0
    index = 0
    lastReleaseMap = dict()
    while index < len(arr):
        if arr[index] in lastReleaseMap:
            timeFromLastRelease = time - lastReleaseMap[arr[index]]
            if timeFromLastRelease > n:
                lastReleaseMap[arr[index]] = time

            else:
                time += n - timeFromLastRelease + 1

        lastReleaseMap[arr[index]] = time
        time += 1
        index += 1

    return time

print(askForCoolingTime([1,1,2,2],
2))