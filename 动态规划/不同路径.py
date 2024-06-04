# 输入：m = 3, n = 7
# 输出：28

def func(m,n):
    if n==1 or m==1:
        return 1
    dp = [[1 for i in range(n)] for j in range(m)]
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]


print(func(3,7))