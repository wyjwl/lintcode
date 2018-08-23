def maxA(N):
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = i
        j = 1
        while j < i - 2:
            dp[i] = max(dp[i], dp[j] * (i - j - 1))
            j += 1
    return dp


print(maxA(9))
