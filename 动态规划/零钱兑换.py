## 用的最少硬币数
class Solution:
    def coinChange(self, coins, amount) -> int:
        '''版本一'''
        # 初始化
        dp = [amount + 1]*(amount + 1)
        dp[0] = 0
        # 遍历物品
        for coin in coins:
            # 遍历背包
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j], dp[j - coin] + 1)

        return dp[amount] if dp[amount] < amount + 1 else -1