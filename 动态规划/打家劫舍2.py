def func(nums):
    res1 = func2(nums[1:])
    res2 = func2(nums[:-1])
    return max(res1,res2)

def func2(nums):
    dp = [0 for i in range(len(nums))]
    dp[0] = nums[0]
    dp[1] = max(nums[1],nums[0])
    for i in range(2,len(nums)):
        dp[i] = max(dp[i-1],dp[i-2]+nums[i])
    return dp[-1]