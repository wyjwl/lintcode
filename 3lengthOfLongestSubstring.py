def lengthOfLongestSubstring(s):
    res = 0
    if s is None or len(s) == 0:
        return res
    d = {}
    start = 0
    for i in range(len(s)):
        if d.__contains__(s[i]) and d[s[i]] >= start:
            start = d[s[i]] + 1
        tmp = i - start + 1
        d[s[i]] = i
        res = max(tmp, res)
    return res

print(lengthOfLongestSubstring("abcabcdfgh"))
