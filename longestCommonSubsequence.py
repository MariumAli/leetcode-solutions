def longestCommonSubSequence(str1, str2):
    dp = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]

    for s1 in range(1, len(str1)+1):
        for s2 in range(1, len(str2)+1):
            if str1[s1-1] == str2[s2-1]:
                dp[s1][s2] = 1 + dp[s1-1][s2-1]
            else:
                dp[s1][s2] = max(dp[s1-1][s2], dp[s1][s2-1])
    print(dp)
    return dp[-1][-1]

print(longestCommonSubSequence('AGGTAB', 'GXTXAYB'))