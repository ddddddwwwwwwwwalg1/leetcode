# 输入: amount = 5, coins = [1, 2, 5]
# 输出: 4
# 解释: 有四种方式可以凑成总金额:
#
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1

class Solution:
    def change(self, amount: int, coins) -> int:
        dp = [0]*(amount + 1)
        dp[0] = 1
        # 遍历物品
        for i in range(len(coins)):
            # 遍历背包 可以重复取一个元素
            for j in range(coins[i], amount + 1):
                dp[j] += dp[j - coins[i]]
        return dp[amount]

