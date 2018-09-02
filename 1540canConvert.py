def canConvert(s, t):
    if t is None:
        return True
    if s is None:
        return False

    if len(s) < len(t):
        return False

    tIndex = 0
    while tIndex < len(t):
        currentChar = t[tIndex]
        if len(s) > 0:
            find = s.find(currentChar)
            if find == -1:
                return False
            else:
                tIndex += 1
                s = s[find + 1 :len(s)]
        else:
            break

    return tIndex == len(t)


print(canConvert("adcadcadcdac", "adddaa"))
