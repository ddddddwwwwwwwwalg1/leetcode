## 'abcde' 'ace' 3
def func(s1,s2):
    dp = [[0 for i in range(len(s1)+1)] for j in range(len(s2)+1)]
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[-1][-1]

