def func(nums):
    dp = nums.copy()
    for i in range(1,len(nums)):
        dp[i] = max(dp[i-1]+nums[i],nums[i])
    return max(dp)
