# [2,7,9,3,1] 输出12
def func(nums):

    dp = [0 for i in range(len(nums))]
    dp[0] = nums[0]
    dp[1] = max(nums[1],nums[0])
    for i in range(2,len(nums)):
        dp[i] = max(dp[i-1],dp[i-2]+nums[i])
    return dp[-1]
