"""
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

示例 1： 输入：s = "abc", t = "ahbgdc" 输出：true

"""

def func(s,t):

    dp = [[0 for i in range(len(t)+1)] for j in range(len(s)+1)]
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]:
                dp[i+1][j+1] = dp[i][j]+1
            else:
                dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
    print(dp)
    return dp[-1][-1] == min(len(s),len(t))

print(func("abc","ahbgdc"))