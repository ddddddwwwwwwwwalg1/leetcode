# cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1] 一次可以爬1或2

def func(cost):
    dp = [0 for i in range(len(cost)+1)]
    for i in range(2, len(cost)+1):
        dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
    return dp[-1]


print(func([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))