def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    bracketStack = []

    if len(s) == 0:
        return False

    for i in range(0, len(s)):
        if s[i] == "(" or s[i] == "[" or s[i] == "{":
            bracketStack.append(s[i])

        if s[i] == ")" or s[i] == "]" or s[i] == "}":
            if len(bracketStack) <= 0 or not isPair(bracketStack.pop(), s[i]):
                return False

    return len(bracketStack) == 0

def isPair(a, b):
    return a=="(" and b==")" or a=="[" and b=="]" or a=="{" and b=="}"

