def reverseWords(s):
    wordList = s.strip().split()
    wordList.reverse()
    result = ""
    for word in wordList:
        result += word + " "

    return result[0 : len(result) - 1]

print(reverseWords("the sky is   blue "))
