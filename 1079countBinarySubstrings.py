def findContiguousNumbers(s, index):
    count = 0
    while index < len(s) - 1:
        if s[index] == s[index + 1]:
            count += 1
            index += 1
        else:
            break

    return index + 1, count + 1, int(s[index])


def countBinarySubstrings(s):
    nextIndex = 0
    l = []
    while nextIndex < len(s):
        nextIndex, count, number = findContiguousNumbers(s, nextIndex)
        l.append([number, count])

    total = 0
    for i in range(1, len(l)):
        n = min(l[i-1][1], l[i][1])
        total += n
    return total


print(countBinarySubstrings("00110011"))
