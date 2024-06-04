# [7,1,5,3,6,4]
# 0持有股票；1不持有股票
def func(nums):
    dp = [[0,0] for _ in range(len(nums))]
    dp[0][0] = -nums[0]
    dp[0][1] = 0
    for i in range(1,len(nums)):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]-nums[i])
        dp[i][1] = max(dp[i-1][1], dp[i-1][0]+nums[i])
    # return dp[-1][1]
    return dp

print(func([7,1,5,3,6,4]))