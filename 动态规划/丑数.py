## 因子为2 3 5
def func(n):
    dp = [1] * n
    a, b, c = 0, 0, 0
    for i in range(1,n):
        n1 = dp[a]*2
        n2 = dp[b]*3
        n3 = dp[c]*5
        dp[i] = min(n1,n2,n3)
        if dp[i] == n1:
            a += 1
        if dp[i] == n2:
            b += 1
        if dp[i] == n3:
            c += 1
    return dp[-1]