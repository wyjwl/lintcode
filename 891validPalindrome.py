def validPalindrome(s):
    start = 0
    end = len(s) - 1

    while start < end:
        if s[start] != s[end]:
            break
        start += 1
        end -= 1

    if start >= end:
        return True

    removeStart = s[0:start]+s[start+1:len(s)]
    removeEnd = s[0:end]+s[end+1:len(s)]

    return isPalindrome(removeStart) or isPalindrome(removeEnd)


def isPalindrome(s):
    return s == s[::-1]

