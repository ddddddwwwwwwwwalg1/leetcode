# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

def func(n):
    dp = [0,1,2]
    if n == 1:
        return 1
    elif n == 2:
        return 2
    for i in range(3,n):
        tmp = dp[i-1] + dp[i-2]
        dp.append(tmp)
    return dp[-1]