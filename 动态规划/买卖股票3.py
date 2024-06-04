# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
# 示例 1: 输入：prices = [3,3,5,0,0,3,1,4] 输出：6

"""
5种状态
0：不操作，
1：第一次持有股票，
2: 第一次不持有股票
3：第二次持有股票
4：第二次不持有股票
"""

def func(prices):
    days = len(prices)
    dp = [[0 for i in range(5)] for j in range(days)]
    dp[0][1] = -prices[0]
    dp[0][3] = -prices[0]
    for i in range(1,days):
        dp[i][0] = dp[i-1][0]
        dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
        dp[i][2] = max(dp[i-1][2], dp[i-1][1]+prices[i])
        dp[i][3] = max(dp[i-1][3], dp[i-1][2]-prices[i])
        dp[i][4] = max(dp[i-1][4], dp[i-1][3]+prices[i])
    return dp[-1][4]



