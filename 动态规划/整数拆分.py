def func(n):
    dp = [0 for _ in range(n+1)]
    for i in range(2,n+1):
        for j in range(i):
            dp[i] = max(dp[i],(i-j)*j,dp[i-j]*j)
    return dp[n]