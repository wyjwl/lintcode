def myAtoi(s):
    """
    :type str: str
    :rtype: int
    """
    s = str.strip(s)

    result = ""
    sign = 1
    for i in range(len(s)):
        if str.isnumeric(s[i]) or (i == 0 and (s[i] == "-" or s[i] == "+")):
            result += s[i]
        else:
            break

    if len(result) == 0:
        return 0

    if result[0] == "-":
        sign = -1
        result = result[1:]
    elif result[0] == "+":
        result = result[1:]

    if str.isnumeric(result):
        finalNumber = sign * int(result)
        if finalNumber <= -2147483648:
            return -2147483648
        if finalNumber >= 2147483647:
            return 2147483647
        return finalNumber
    return 0

print(myAtoi("-5-"))